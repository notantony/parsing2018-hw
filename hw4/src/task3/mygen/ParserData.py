from LexerData import *

class nonterm:
    pass

class start(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitstart(self)

class statements(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitstatements(self)

class idents(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitidents(self)

class statement(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitstatement(self)

class ifC(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitifC(self)

class ifPost(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitifPost(self)

class whileC(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitwhileC(self)

class assignment(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitassignment(self)

class expr(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitexpr(self)

class action(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitaction(self)

start.rules = [(IDENT, idents, ASSIGNMENT, statements, EOF,)]
start.first = {IDENT: 0}
start.follow = {}
start.links = [('_varid', '_varids', None, '_varsts', None)]
start.rule = '_var0.name = _varid\n_var0.sts = _varsts.sts\n_var0.vars = _varids.ids'
start.defs = {'_var0': None, '_varid': None, '_varsts': None, '_varids': None}

statements.rules = [(), (statement, statements,)]
statements.first = {(): 0, LPAR: 1, IF: 1, WHILE: 1, ASSIGNMENT: 1, CONSUMER1: 1}
statements.follow = {EOF, RPAR}
statements.links = [(), ('_varthis', '_varalso')]
statements.rule = 'if _varthis is None:\n    _var0.sts = []\nelse:\n    _var0.sts = [_varthis] + _varalso.sts'
statements.defs = {'_varthis': None, '_var0': None, '_varalso': None}

idents.rules = [(IDENT, idents,), ()]
idents.first = {IDENT: 0, (): 1}
idents.follow = {ASSIGNMENT}
idents.links = [('_varthis', '_varalso'), ()]
idents.rule = 'if _varthis is None:\n    _var0.ids = []\nelse:\n    _var0.ids = [_varthis] + _varalso.ids'
idents.defs = {'_varthis': None, '_var0': None, '_varalso': None}

statement.rules = [(assignment,), (action,), (LPAR, statement, statements, RPAR,), (ifC,), (whileC,)]
statement.first = {LPAR: 2, IF: 3, WHILE: 4, ASSIGNMENT: 0, CONSUMER1: 1}
statement.follow = {WHILE, LPAR, CONSUMER1, IF, ASSIGNMENT, RPAR, EOF}
statement.links = [(None,), (None,), (None, '_varthis', '_varalso', None), (None,), (None,)]
statement.rule = 'if _varthis is not None:\n    _var0.sts = [_varthis] + _varalso.sts'
statement.defs = {'_varthis': None, '_var0': None, '_varalso': None}

ifC.rules = [(IF, expr, statement, ifPost,)]
ifC.first = {IF: 0}
ifC.follow = {WHILE, LPAR, CONSUMER1, IF, ASSIGNMENT, RPAR, EOF}
ifC.links = [(None, '_varexpr', '_varstat', '_varpost')]
ifC.rule = '_var0.COND = "if (" + _varexpr.STR + ") "\n_var0.stat = _varstat\n_var0.post = _varpost'
ifC.defs = {'_var0': None, '_varexpr': None, '_varstat': None, '_varpost': None}

ifPost.rules = [(), (statement,)]
ifPost.first = {(): 0, LPAR: 1, IF: 1, WHILE: 1, ASSIGNMENT: 1, CONSUMER1: 1}
ifPost.follow = {WHILE, LPAR, CONSUMER1, IF, ASSIGNMENT, RPAR, EOF}
ifPost.links = [(), ('_varstat',)]
ifPost.rule = '_var0.post = _varstat'
ifPost.defs = {'_var0': None, '_varstat': None}

whileC.rules = [(WHILE, expr, statement,)]
whileC.first = {WHILE: 0}
whileC.follow = {WHILE, LPAR, CONSUMER1, IF, ASSIGNMENT, RPAR, EOF}
whileC.links = [(None, '_varexpr', '_varstat')]
whileC.rule = '_var0.COND = "while (" + _varexpr.STR + ") "\n_var0.stat = _varstat'
whileC.defs = {'_var0': None, '_varexpr': None, '_varstat': None}

assignment.rules = [(ASSIGNMENT, IDENT, expr,)]
assignment.first = {ASSIGNMENT: 0}
assignment.follow = {WHILE, LPAR, CONSUMER1, IF, ASSIGNMENT, RPAR, EOF}
assignment.links = [(None, '_varid', '_varexpr')]
assignment.rule = '_var0.IDENT = _varid\n_var0.STR = _varid + " = " + _varexpr.STR'
assignment.defs = {'_var0': None, '_varid': None, '_varexpr': None}

expr.rules = [(IDENT,), (CONST,), (LPAR, expr, RPAR,), (OPERATOR2, expr, expr,)]
expr.first = {IDENT: 0, CONST: 1, LPAR: 2, OPERATOR2: 3}
expr.follow = {WHILE, CONST, LPAR, CONSUMER1, IF, OPERATOR2, ASSIGNMENT, RPAR, IDENT, EOF}
expr.links = [('_varid',), ('_varc',), (None, '_vare', None), ('_varop', '_vara1', '_vara2')]
expr.rule = 'if _varc is not None:\n    if _varc == "true":\n        _var0.val = 1\n    elif _varc == "false":\n        _var0.val = 0\n    else:\n        _var0.val = int(_varc)\nelif _varop is not None:\n    if getattr(_vara1, "val", None) is not None and getattr(_vara2, "val", None) is not None:\n        if _varop in "+-*%<>" or _varop == ">=" or _varop == "<=" or _varop == "!=" or _varop == "==":\n            _var0.val = int(eval(str(_vara1.val) + _varop + str(_vara2.val)))\n        elif _varop == "&&":\n            _var0.val = int(bool(_vara1.val and _vara2.val))\n        elif _varop == "||":\n            _var0.val = int(bool(_vara1.val or _vara2.val))\n        else:\n            _var0.val = _vara1.val // _vara2.val\n        print("Optimized: " + str(_vara1.val) + _varop + str(_vara2.val) + " = " + str(_var0.val))\nelif _varid is not None:\n    _var0.STR = _varid\nelif _vare is not None:\n    if hasattr(_vare, "val"):\n        _var0.val = _vare.val\n    else:\n        _var0.STR = "(" + _vare.STR + ")"\nif hasattr(_var0, "val"):\n    _var0.STR = str(_var0.val)\nif not hasattr(_var0, "STR"):\n    _var0.STR = ("(" + _vara1.STR + " " + _varop + " " + _vara2.STR + ")")'
expr.defs = {'_varc': None, '_var0': None, '_varop': None, '_vara1': None, '_vara2': None, '_varid': None, '_vare': None}

action.rules = [(CONSUMER1, expr,)]
action.first = {CONSUMER1: 0}
action.follow = {WHILE, LPAR, CONSUMER1, IF, ASSIGNMENT, RPAR, EOF}
action.links = [('_varC', '_varexpr')]
action.rule = '_var0.STR = "std::cout << " + _varexpr.STR'
action.defs = {'_var0': None, '_varexpr': None}

