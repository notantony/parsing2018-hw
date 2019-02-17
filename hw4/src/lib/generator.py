import os
import sys
import importlib

from antlr4 import *

from ParserVisitor import ParserVisitor
from LexerVisitor import LexerVisitor
from MainLexer import MainLexer
from MainParser import MainParser

def main(argv):
    parse(argv[1], argv[2])

def parse(inputFileName, outputDir = "mygen"):
    input = FileStream(inputFileName)
    lexer = MainLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MainParser(stream)
    tree = parser.start()
    with open(os.path.join(outputDir, "LexerData.py"), "w") as lexerFile:
        lexerFile.write("import re\n\nclass term:\n    pass\n\nclass EOF(term):\n    def __init__(self):\n        self.pos = (EOF, EOF)\n        self.data = 'EOF'\n    def visit(self, c):\n        pass\n\n")
        tokens = LexerVisitor(lexerFile).visit(tree)
        print("lexer generated")
    with open(os.path.join(outputDir, "ParserData.py"), "w") as parserFile:
        parserFile.write("from LexerData import *\n\nclass nonterm:\n    pass\n\n")
        parser = ParserVisitor(parserFile, tokens)
        parser.visit(tree)
        print("parser generated")
    with open(os.path.join(outputDir, "MyVisitor.py"), "w") as visitorFile:
        visitorFile.write("class MyVisitor:\n")
        visitorFile.write("    def visitChildren(self, c):\n        if c.children is not None:\n            for one in c.children:\n                one.visit(self)\n\n")
        for t in tokens[1:]:
            visitorFile.write("    def visit{}(self, c):\n        pass\n\n".format(t))
        for t in parser.data:
            visitorFile.write("    def visit{}(self, c):\n        self.visitChildren(c)\n\n".format(t))
        print("visitor generated")


if __name__ == '__main__':
    main(sys.argv)