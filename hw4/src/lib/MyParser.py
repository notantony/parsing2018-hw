from ParserData import *
from lib.MyLexer import *

class ParsingError(RuntimeError):
    def __init__(self, message = ""):
        super().__init__(message)

class MyParser:
    def __init__(self, lexer: MyLexer):
        self.lexer = lexer
        self.result = None
        self.iter = self.lexer.nextToken()
        self.curToken = None
        self.nextToken()

    def parse(self):
        return self._run(start)

    def token(self, expect = None):
        token = self.curToken
        if expect is not None and type(token) not in expect:
            raise ParsingError("Unexpected token: {}, expected: {}, line: {}, pos: {}".format(type(token), expect, token.pos[0], token.pos[1]))
        return token

    def nextToken(self):
        self.curToken = next(self.iter, None)


    def _run(self, cur):
        expecting = set(cur.first.keys()) | (set(cur.follow) if () in cur.first.keys() else set())
        token = self.token(expecting)
        rule = cur.first.get(type(token))
        ret = cur()
        if cur.defs is not None:
            loc = cur.defs.copy()
        else:
            loc = {}
        loc["_var0"] = ret
        if rule is not None:
            ret.children = []
            i = 0
            for x in cur.rules[rule]:
                if issubclass(x, term):
                    ret.children.append(self.token([x]))
                    loc[cur.links[rule][i]] = self.token().data
                    self.nextToken()
                else:
                    tmp = self._run(x)
                    ret.children.append(tmp)
                    loc[cur.links[rule][i]] = tmp
                i += 1
        elif () in cur.first and type(token) in cur.follow:
            ret.children = None
        else:
            raise ParsingError("Unexpected token: {}, expected: {}, line: {}, pos: {}".format(token, expecting, token.pos[0], token.pos[1]))
        if cur.rule is not None:
            try:
                exec(cur.rule, loc)
            except Exception as e:
                print(e)
                raise ParsingError("Computation failed for rule: {}\ncode:\n{}\nlocals:\n{}\n".format(cur, cur.rule, loc))
        return ret

    def dfs(self, cur):
        ret = "\n" + str(type(cur))
        if issubclass(type(cur), term):
            return ret
        if cur.children is None:
            return ret + ": EPS"
        ret += ": {"
        for one in cur.children:
            ret += self.dfs(one) + ", "
        return ret + "}"