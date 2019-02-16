from lexer import *

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

statements.rules = [(statement, statements,), ()]
statements.first = {(): 1, LPAR: 0, IF: 0, WHILE: 0, ASSIGNMENT: 0, CONSUMER1: 0}
statements.follow = {RPAR, EOF}
statements.links = [(None, None), ()]
statements.rule = None

name.rules = [(IDENT,)]
name.first = {IDENT: 0}
name.follow = {IDENT, ASSIGNMENT}
name.links = [(None,)]
name.rule = None

vars.rules = [(idents,)]
vars.first = {IDENT: 0, (): 0}
vars.follow = {ASSIGNMENT}
vars.links = [(None,)]
vars.rule = None

idents.rules = [(IDENT, idents,), ()]
idents.first = {IDENT: 0, (): 1}
idents.follow = {ASSIGNMENT}
idents.links = [(None, None), ()]
idents.rule = None

program.rules = [(statement, statements,)]
program.first = {LPAR: 0, IF: 0, WHILE: 0, ASSIGNMENT: 0, CONSUMER1: 0}
program.follow = {RPAR}
program.links = [(None, None)]
program.rule = None

statement.rules = [(action,), (assignment,), (LPAR, program, RPAR,), (ifC,), (whileC,)]
statement.first = {LPAR: 2, IF: 3, WHILE: 4, ASSIGNMENT: 1, CONSUMER1: 0}
statement.follow = {RPAR, IF, EOF, LPAR, WHILE, CONSUMER1, ASSIGNMENT}
statement.links = [(None,), (None,), (None, None, None), (None,), (None,)]
statement.rule = None

ifC.rules = [(IF, expr, statement, ifPost,)]
ifC.first = {IF: 0}
ifC.follow = {RPAR, IF, EOF, LPAR, WHILE, CONSUMER1, ASSIGNMENT}
ifC.links = [(None, None, None, None)]
ifC.rule = None

ifPost.rules = [(), (statement,)]
ifPost.first = {(): 0, LPAR: 0, IF: 0, WHILE: 0, ASSIGNMENT: 0, CONSUMER1: 0}
ifPost.follow = {RPAR, IF, EOF, LPAR, WHILE, CONSUMER1, ASSIGNMENT}
ifPost.links = [(), (None,)]
ifPost.rule = None

whileC.rules = [(WHILE, expr, statement,)]
whileC.first = {WHILE: 0}
whileC.follow = {RPAR, IF, EOF, LPAR, WHILE, CONSUMER1, ASSIGNMENT}
whileC.links = [(None, None, None)]
whileC.rule = None

assignment.rules = [(ASSIGNMENT, IDENT, expr,)]
assignment.first = {ASSIGNMENT: 0}
assignment.follow = {RPAR, IF, EOF, LPAR, WHILE, CONSUMER1, ASSIGNMENT}
assignment.links = [(None, None, None)]
assignment.rule = None

expr.rules = [(CONST,), (OPERATOR2, expr, expr,), (LPAR, expr, RPAR,), (IDENT,)]
expr.first = {CONST: 0, OPERATOR2: 1, LPAR: 2, IDENT: 3}
expr.follow = {RPAR, IF, EOF, LPAR, IDENT, WHILE, CONSUMER1, ASSIGNMENT, CONST, OPERATOR2}
expr.links = [('@1',), (None, '@2', '@3'), (None, None, None), (None,)]
expr.rule = "if @1 is not None:\n    print('This is const = ' + @1)"

action.rules = [(CONSUMER1, expr,)]
action.first = {CONSUMER1: 0}
action.follow = {RPAR, IF, EOF, LPAR, WHILE, CONSUMER1, ASSIGNMENT}
action.links = [(None, None)]
action.rule = None

