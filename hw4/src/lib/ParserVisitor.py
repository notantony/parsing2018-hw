import re, itertools, operator
from MainVisitor import MainVisitor
from MainParser import MainParser

class BuildError(RuntimeError):
    def __init__(self, message = ""):
        super().__init__(message)

def is_term(s : str):
    return s[0].isupper()

class ParserVisitor(MainVisitor):
    @staticmethod
    def getid(ctx):
        if ctx.AT() is not None:
            return ctx.AT().getText().replace("@", "_var")

    @staticmethod
    def gettext(ctx):
        if ctx.LOWER_IDENT() is not None:
            return ctx.LOWER_IDENT().getText()
        return ctx.CAPS_IDENT().getText()

    @staticmethod
    def brush(s: str):
        s = s.replace("\t", "    ")
        s.strip(" ")
        s = s.strip("{}")
        s = s.strip("\n\r")
        split = s.splitlines(False)
        if split == []:
            return ""
        cut = 0
        while cut < len(s) and s[cut] == ' ':
            cut += 1
        return repr("\n".join([s[cut:] for s in split]))

    @staticmethod
    def wlist(a):
        return "[" + ", ".join(map(lambda x: "(" + " ".join(map(lambda t : t + ",", x)) + ")", a)) + "]"

    @staticmethod
    def wdict(d):
        return "{" + ", ".join(map(lambda x: str(x) + ": " + str(d[x]), d)) + "}"

    @staticmethod
    def wset(s):
        return "{" + ", ".join(map(str, s)) + "}"

    def __init__(self, output, tokens):
        self.output = output
        self.tokens = tokens
        self.st = set()
        self.data = {}
        self.first = {}
        self.follow = {}
        self.links = {}
        self.attr = {}
        self.defs = {}

    def put_first(self, nt, token, index):
        if self.first[nt].get(token) is not None and self.first[nt].get(token) != index:
            raise BuildError("Right branching was found for non-terminal: " + nt + ", token: " + token)
        if self.first[nt].get(token) == index:
            return False
        self.first[nt][token] = index
        return True

    def put_follow(self, nt, token):
        if token in self.follow[nt]:
            return False
        self.follow[nt].add(token)
        return True

    def check_def(self):
        for nt in self.data:
            for rule in self.data[nt]:
                if rule == ():
                    continue
                for x in rule:
                    if is_term(x) and x not in self.tokens:
                        raise BuildError("Unexpected terminal was found: <{}> for non-terminal: <{}>".format(x, nt))
                    elif not is_term(x) and x not in self.data:
                        raise BuildError("Unexpected non-terminal was found: <{}> for non-terminal: <{}>".format(x, nt))

    def check_rr(self, nt):
        if nt in self.st:
            raise BuildError("Right recursion was found for non-terminal: " + nt)
        self.st.add(nt)
        for rule in self.data[nt]:
            if rule != () and not is_term(rule[0]):
                self.check_rr(rule[0])
        self.st.remove(nt)

    def build_first(self):
        upd = True
        while upd:
            upd = False
            for nt in self.data:
                index = -1
                for rule in self.data[nt]:
                    index += 1
                    if rule == ():
                        upd = upd or self.put_first(nt, (), index)
                        continue
                    eps = True
                    for x in rule:
                        if not eps:
                            break
                        eps = False
                        if is_term(x):
                            upd = upd or self.put_first(nt, x, index)
                            break
                        for token in self.first[x]:
                            if token == ():
                                eps = True
                            else:
                                upd = upd or self.put_first(nt, token, index)
                    if eps:
                        upd = upd or self.put_first(nt, (), index)

    def build_follow(self):
        upd = True
        while upd:
            upd = False
            for nt in self.data:
                for rule in self.data[nt]:
                    queries = set()
                    for x in rule:
                        if is_term(x):
                            for q in queries:
                                upd = upd or self.put_follow(q, x)
                            queries = set()
                        else:
                            for q in queries:
                                for y in self.first[q]:
                                    if y != ():
                                        upd = upd or self.put_follow(q, y)
                            if () not in self.first[x]:
                                queries = set()
                            queries.add(x)
                    for q in queries:
                        for y in self.follow[nt]:
                            upd = upd or self.put_follow(q, y)

    def build(self):
        self.check_def()
        for nt in self.data:
            self.check_rr(nt)
        self.build_first()
        self.build_follow()

    def visitStart(self, ctx:MainParser.StartContext):
        for rule in ctx.parsingRule():
            nt, rules, attr = self.visit(rule)
            self.first[nt] = {}
            self.follow[nt] = set()
            self.data[nt] = set(rules)
            if attr is not None:
                code = ParserVisitor.brush(attr.getText())
                defs = {}
                for x in re.findall("@[\d\w]+", code):
                    defs[str(x).replace("@", "_var")] = None
                self.defs[nt] = defs
                self.attr[nt] = code.replace("@", "_var")
            else:
                self.attr[nt] = None
                self.defs[nt] = None
        for nt in self.data:
            self.links[nt] = [tuple(map(ParserVisitor.getid, x)) for x in self.data[nt]]
            self.data[nt] = [tuple(map(ParserVisitor.gettext, x)) for x in self.data[nt]]
        self.build()
        for nt in self.data:
            self.output.write("class {}(nonterm):\n    def __init__(self):\n        pass\n    def visit(self, visitor):\n        visitor.visit{}(self)\n\n".format(nt, nt))
        for nt in self.data:
            self.output.write("{0}.rules = {1}\n{0}.first = {2}\n{0}.follow = {3}\n{0}.links = {4}\n{0}.rule = {5}\n{0}.defs = {6}\n\n".format(nt, self.wlist(self.data[nt]), self.wdict(self.first[nt]), self.wset(self.follow[nt]), self.links[nt], self.attr[nt], self.defs[nt]))


    def visitParsingRule(self, ctx:MainParser.ParsingRuleContext):
        rules = self.visit(ctx.parsingExpr())
        return ctx.LOWER_IDENT().getText(), rules, ctx.CODE()

    def visitParsingExpr(self, ctx:MainParser.ParsingExprContext):
        if ctx.LPAR() is not None:
            return self.visit(ctx.parsingExpr(0))
        if ctx.BAR() is not None:
            return self.visit(ctx.parsingExpr(0)) + self.visit(ctx.parsingExpr(1))
        solo = self.visit(ctx.parsingSolo())
        if ctx.parsingExpr(0) is not None:
            expr = self.visit(ctx.parsingExpr(0))
            return [x + y for x in solo for y in expr]
        return solo

    def visitParsingSolo(self, ctx:MainParser.ParsingSoloContext):
        if ctx.CAPS_IDENT() is not None:
            if ctx.CAPS_IDENT().getText() == "EPS":
                if ctx.AT() is not None:
                    raise BuildError("EPS cannot be referenced")
                return [()]
        return [(ctx,)]


del MainParser