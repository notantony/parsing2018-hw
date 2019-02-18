import sys

from lib.MyLexer import MyLexer
from lib.MyParser import MyParser
from task3.Visitor3 import Visitor3


def main(inputFile, outputFile = "output.txt"):
    with open(inputFile, "r") as test:
        lexer = MyLexer(test)
        parser = MyParser(lexer)
        tree = parser.parse()
    with open(outputFile, "w") as outputFile:
        tree.visit(Visitor3(outputFile))


if __name__ == '__main__':
    main(sys.argv[1])