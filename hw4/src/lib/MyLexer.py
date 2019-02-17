from LexerData import *

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
                        yield token(match.group(), (lineN, pos + match.start(), match.end()))
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

