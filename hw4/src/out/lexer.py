import re

class term:
    pass

class EOF(term):
    def __init__(self):
        self.pos = (EOF, EOF)

class IF(term):
    regexp = r"if"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class WHILE(term):
    regexp = r"while"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class CONST(term):
    regexp = r"\d+|(true)|(false)"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class CONSUMER1(term):
    regexp = r"print"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class OPERATOR2(term):
    regexp = r"(&&)|(\|\|)|(>=)|(<=)|(==)|(!=)|[+-/*%<>]"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class ASSIGNMENT(term):
    regexp = r"="
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class IDENT(term):
    regexp = r"([a-zA-z]|_)([a-zA-z]|[0-9]|_)*"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class LPAR(term):
    regexp = r"\("
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

class RPAR(term):
    regexp = r"\)"
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos

tokens = [EOF, IF, WHILE, CONST, CONSUMER1, OPERATOR2, ASSIGNMENT, IDENT, LPAR, RPAR]

class LexingError(RuntimeError):
    def __init__(self, message = ""):
        super().__init__(message)

class MyLexer:
    def __init__(self, inputFile):
        self.inputFile = inputFile

    def nextToken(self):
        lineN = 0
        for line in self.inputFile.readlines():
            pos = 0
            lineN += 1
            while pos < len(line):
                ok = False
                for token in tokens[1:]:
                    match = re.search(token.regexp, line[pos:])
                    if match is not None and pos + match.start() == pos:
                        yield token(match.string, (lineN, pos + match.start(), match.end()))
                        pos += match.end()
                        ok = True
                        break
                if ok:
                    continue
                else:
                    if line[pos] in " \n\t\r\f":
                        pos += 1
                    else:
                        raise LexingError("Unexpected lexema, line {}, position {}".format(lineN, pos + 1))
        yield EOF()

