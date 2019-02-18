import sys

from lib.MyLexer import MyLexer
from lib.MyParser import MyParser
from task2.Visitor2 import Visitor2


def main(inputFile, outputFile = "output.txt"):
    with open(inputFile, "r") as test:
        lexer = MyLexer(test)
        parser = MyParser(lexer)
        tree = parser.parse()
    with open(outputFile, "w") as outputFile:
        tree.visit(Visitor2(outputFile))


if __name__ == '__main__':
    main(sys.argv[1])