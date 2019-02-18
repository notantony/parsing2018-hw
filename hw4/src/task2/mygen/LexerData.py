import re

class term:
    pass

class EOF(term):
    def __init__(self):
        self.pos = (EOF, EOF)
        self.data = 'EOF'
    def visit(self, c):
        pass

class LBRACKET(term):
    regexp = r"\("
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitLBRACKET(self)

class RBRACKET(term):
    regexp = r"\)"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitRBRACKET(self)

class PTR(term):
    regexp = r"\*"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitPTR(self)

class SEMICOLON(term):
    regexp = r";"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitSEMICOLON(self)

class COMMA(term):
    regexp = r","
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitCOMMA(self)

class IDENT(term):
    regexp = r"[_a-zA-Z]\w*"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitIDENT(self)

tokens = [EOF, LBRACKET, RBRACKET, PTR, SEMICOLON, COMMA, IDENT]

