from out.lexer import *

class nonterm:
    pass

_init = 'print("Parsing started")'

class start(nonterm):
    def __init__(self):
        self.__attr__ = {}

class statements(nonterm):
    def __init__(self):
        self.__attr__ = {}

class name(nonterm):
    def __init__(self):
        self.__attr__ = {}

class vars(nonterm):
    def __init__(self):
        self.__attr__ = {}

class idents(nonterm):
    def __init__(self):
        self.__attr__ = {}

class program(nonterm):
    def __init__(self):
        self.__attr__ = {}

class statement(nonterm):
    def __init__(self):
        self.__attr__ = {}

class ifC(nonterm):
    def __init__(self):
        self.__attr__ = {}

class ifPost(nonterm):
    def __init__(self):
        self.__attr__ = {}

class whileC(nonterm):
    def __init__(self):
        self.__attr__ = {}

class assignment(nonterm):
    def __init__(self):
        self.__attr__ = {}

class expr(nonterm):
    def __init__(self):
        self.__attr__ = {}

class action(nonterm):
    def __init__(self):
        self.__attr__ = {}

start.rules = [(name, vars, ASSIGNMENT, statement, statements, EOF,)]
start.first = {IDENT: 0}
start.follow = {}
start.links = [(None, None, None, None, None, None)]
start.rule = None

statements.rules = [(), (statement, statements,)]
statements.first = {(): 0, LPAR: 0, IF: 0, WHILE: 0, ASSIGNMENT: 0, CONSUMER1: 0}
statements.follow = {RPAR, EOF}
statements.links = [(), (None, None)]
statements.rule = None

name.rules = [(IDENT,)]
name.first = {IDENT: 0}
name.follow = {IDENT, ASSIGNMENT}
name.links = [(None,)]
name.rule = None

vars.rules = [(idents,)]
vars.first = {(): 0, IDENT: 0}
vars.follow = {ASSIGNMENT}
vars.links = [(None,)]
vars.rule = None

idents.rules = [(), (IDENT, idents,)]
idents.first = {(): 0, IDENT: 0}
idents.follow = {ASSIGNMENT}
idents.links = [(), (None, None)]
idents.rule = None

program.rules = [(statement, statements,)]
program.first = {LPAR: 0, IF: 0, WHILE: 0, ASSIGNMENT: 0, CONSUMER1: 0}
program.follow = {RPAR}
program.links = [(None, None)]
program.rule = None

statement.rules = [(action,), (assignment,), (ifC,), (whileC,), (LPAR, program, RPAR,)]
statement.first = {LPAR: 4, IF: 2, WHILE: 3, ASSIGNMENT: 1, CONSUMER1: 0}
statement.follow = {RPAR, IF, CONSUMER1, EOF, ASSIGNMENT, WHILE, LPAR}
statement.links = [(None,), (None,), (None,), (None,), (None, None, None)]
statement.rule = None

ifC.rules = [(IF, expr, statement, ifPost,)]
ifC.first = {IF: 0}
ifC.follow = {RPAR, IF, EOF, CONSUMER1, ASSIGNMENT, WHILE, LPAR}
ifC.links = [(None, None, None, None)]
ifC.rule = None

ifPost.rules = [(statement,), ()]
ifPost.first = {LPAR: 0, IF: 0, (): 1, WHILE: 0, ASSIGNMENT: 0, CONSUMER1: 0}
ifPost.follow = {RPAR, IF, EOF, CONSUMER1, ASSIGNMENT, WHILE, LPAR}
ifPost.links = [(None,), ()]
ifPost.rule = None

whileC.rules = [(WHILE, expr, statement,)]
whileC.first = {WHILE: 0}
whileC.follow = {RPAR, IF, EOF, CONSUMER1, ASSIGNMENT, WHILE, LPAR}
whileC.links = [(None, None, None)]
whileC.rule = None

assignment.rules = [(ASSIGNMENT, IDENT, expr,)]
assignment.first = {ASSIGNMENT: 0}
assignment.follow = {RPAR, IF, EOF, CONSUMER1, ASSIGNMENT, WHILE, LPAR}
assignment.links = [(None, None, None)]
assignment.rule = None

expr.rules = [(LPAR, expr, RPAR,), (CONST,), (OPERATOR2, expr, expr,), (IDENT,)]
expr.first = {LPAR: 0, CONST: 1, OPERATOR2: 2, IDENT: 3}
expr.follow = {RPAR, IF, EOF, CONSUMER1, ASSIGNMENT, OPERATOR2, CONST, LPAR, WHILE, IDENT}
expr.links = [(None, None, None), ('@1',), (None, '@2', '@3'), (None,)]
expr.rule = "if @1 is not None:\n    print('This is const = ' + @1)"

action.rules = [(CONSUMER1, expr,)]
action.first = {CONSUMER1: 0}
action.follow = {RPAR, IF, EOF, CONSUMER1, ASSIGNMENT, WHILE, LPAR}
action.links = [(None, None)]
action.rule = None


class ParsingError(RuntimeError):
    def __init__(self, message = ""):
        super().__init__(message)

class MyParser:
    def __init__(self, lexer: MyLexer):
        self.lexer = lexer
        self.result = None
        self.iter = self.lexer.nextToken()
        self.nextToken()
        self.globals = globals().copy()

    def parse(self):
        exec(_init, self.globals)
        print(self.dfs(self._run(start)))

    def token(self, expect = None):
        token = self.curToken
        if expect is not None and type(token) not in expect:
            raise ParsingError("Unexpected token: {}, expected: {}, line: {}, pos: {}".format(type(token), expect, token.pos[0], token.pos[1]))
        return token

    def nextToken(self, expect = None):
        self.curToken = next(self.iter, None)



    def _run(self, cur):
        expecting = set(cur.first.keys()) | (set(cur.follow) if () in cur.first.keys() else set())
        token = self.token(expecting)
        rule = cur.first.get(type(token))
        ret = cur()
        if rule is not None:
            ret.children = []
            for x in cur.rules[rule]:
                if issubclass(x, term):
                    ret.children.append(self.token([x]))
                    self.nextToken()
                else:
                    ret.children.append(self._run(x))
        elif () in cur.first and type(token) in cur.follow:
            ret.children = None
        else:
            raise ParsingError("Unexpected token: {}, expected: {}, line: {}, pos: {}".format(token, expecting, token.pos[0], token.pos[1]))
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