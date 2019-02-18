from LexerData import *

class nonterm:
    pass

class start(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitstart(self)

class type_(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visittype_(self)

class args(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitargs(self)

class args_(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitargs_(self)

class modifier(nonterm):
    def __init__(self):
        pass
    def visit(self, visitor):
        visitor.visitmodifier(self)

start.rules = [(type_, IDENT, LBRACKET, args, RBRACKET, SEMICOLON,)]
start.first = {IDENT: 0}
start.follow = {}
start.links = [(None, None, None, None, None, None)]
start.rule = '_var0.data = "S"'
start.defs = {'_var0': None}

type_.rules = [(IDENT, modifier,)]
type_.first = {IDENT: 0}
type_.follow = {IDENT}
type_.links = [(None, None)]
type_.rule = '_var0.data = "T"'
type_.defs = {'_var0': None}

args.rules = [(type_, IDENT, args_,), ()]
args.first = {IDENT: 0, (): 1}
args.follow = {RBRACKET}
args.links = [(None, None, None), ()]
args.rule = 'if _varne is not None:\n    _var0.ne = True\n_var0.data = "A"'
args.defs = {'_varne': None, '_var0': None}

args_.rules = [(), (COMMA, type_, IDENT, args_,)]
args_.first = {(): 0, COMMA: 1}
args_.follow = {RBRACKET}
args_.links = [(), (None, '_varne', None, None)]
args_.rule = 'if _varne is not None:\n    _var0.ne = True\n_var0.data = "A\'"'
args_.defs = {'_varne': None, '_var0': None}

modifier.rules = [(PTR, modifier,), ()]
modifier.first = {PTR: 0, (): 1}
modifier.follow = {IDENT}
modifier.links = [(None, '_varne'), ()]
modifier.rule = 'if _varne is not None:\n    _var0.ne = True\n_var0.data = "M"'
modifier.defs = {'_varne': None, '_var0': None}

