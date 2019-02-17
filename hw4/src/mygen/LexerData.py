import re

class term:
    pass

class EOF(term):
    def __init__(self):
        self.pos = (EOF, EOF)
        self.data = 'EOF'
    def visit(self, c):
        pass

class IF(term):
    regexp = r"if"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitIF(self)

class WHILE(term):
    regexp = r"while"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitWHILE(self)

class CONST(term):
    regexp = r"\d+|(true)|(false)"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitCONST(self)

class CONSUMER1(term):
    regexp = r"print"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitCONSUMER1(self)

class OPERATOR2(term):
    regexp = r"(&&)|(\|\|)|(>=)|(<=)|(==)|(!=)|[+-/*%<>]"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitOPERATOR2(self)

class ASSIGNMENT(term):
    regexp = r"="
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitASSIGNMENT(self)

class IDENT(term):
    regexp = r"([a-zA-z]|_)([a-zA-z]|[0-9]|_)*"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitIDENT(self)

class LPAR(term):
    regexp = r"\("
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitLPAR(self)

class RPAR(term):
    regexp = r"\)"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
    def visit(self, visitor):
        visitor.visitRPAR(self)

tokens = [EOF, IF, WHILE, CONST, CONSUMER1, OPERATOR2, ASSIGNMENT, IDENT, LPAR, RPAR]

