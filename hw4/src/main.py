import sys, os
from antlr4 import *
from MainLexer import MainLexer
from MainParser import MainParser
from LexerVisitor import LexerVisitor
from ParserVisitor import ParserVisitor


def main(argv):
    if True:
        from out.lexer import MyLexer
        from tmp import MyParser
        with open("test.txt") as test:
            lexer = MyLexer(test)
            #print(list(lexer.nextToken()))
            parser = MyParser(lexer)
            tree = parser.parse()
    else:
        parse(argv[1], argv[2])

def parse(inputFileName, outputDir = "out", parserName = "My"):
    input = FileStream(inputFileName)
    lexer = MainLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MainParser(stream)
    tree = parser.start()
    with open(os.path.join(outputDir, "lexer.py"), "w") as lexerFile:
        lexerFile.write("import re\n\nclass term:\n    pass\n\nclass EOF(term):\n    def __init__(self):\n        self.pos = (EOF, EOF)\n\n")
        tokens = LexerVisitor(lexerFile).visit(tree)
        lexerFile.write("class LexingError(RuntimeError):\n    def __init__(self, message = \"\"):\n        super().__init__(message)\n\n")
        lexerFile.write("class {}Lexer:\n    def __init__(self, inputFile):\n        self.inputFile = inputFile\n\n    def nextToken(self):\n        lineN = 0\n        for line in self.inputFile.readlines():\n            pos = 0\n            lineN += 1\n            while pos < len(line):\n                ok = False\n                for token in tokens[1:]:\n                    match = re.search(token.regexp, line[pos:])\n                    if match is not None and pos + match.start() == pos:\n                        yield token(match.string, (lineN, pos + match.start(), match.end()))\n                        pos += match.end()\n                        ok = True\n                        break\n                if ok:\n                    continue\n                else:\n                    if line[pos] in \" \\n\\t\\r\\f\":\n                        pos += 1\n                    else:\n                        raise LexingError(\"Unexpected lexema, line {}, position {}\".format(lineN, pos + 1))\n        yield EOF()\n\n".format(parserName, "{}", "{}"))
    with open(os.path.join(outputDir, "parser.py"), "w") as parserFile:
        parserFile.write("from lexer import *\n\nclass nonterm:\n    pass\n\n")
        ParserVisitor(parserFile, tokens).visit(tree)


if __name__ == '__main__':
    main(sys.argv)