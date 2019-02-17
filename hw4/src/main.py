from lib.MyParser import MyParser
from lib.MyLexer import MyLexer
from Visitor3 import Visitor3
import sys

def main(inputFile, outputFile = "output.txt"):
    with open(inputFile, "r") as test:
        lexer = MyLexer(test)
        parser = MyParser(lexer)
        tree = parser.parse()
    with open(outputFile, "w") as outputFile:
        tree.visit(Visitor3(outputFile))


if __name__ == '__main__':
    main(sys.argv[1])