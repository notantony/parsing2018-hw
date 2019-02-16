# Generated from ../src/Test.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("-\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\3\2\2\2,\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2")
        buf.write("\2\5\31\3\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13\37\3\2\2")
        buf.write("\2\r!\3\2\2\2\17#\3\2\2\2\21%\3\2\2\2\23\'\3\2\2\2\25")
        buf.write(")\3\2\2\2\27\30\7c\2\2\30\4\3\2\2\2\31\32\7d\2\2\32\6")
        buf.write("\3\2\2\2\33\34\7e\2\2\34\b\3\2\2\2\35\36\7f\2\2\36\n\3")
        buf.write("\2\2\2\37 \7g\2\2 \f\3\2\2\2!\"\7h\2\2\"\16\3\2\2\2#$")
        buf.write("\7i\2\2$\20\3\2\2\2%&\7j\2\2&\22\3\2\2\2\'(\7m\2\2(\24")
        buf.write("\3\2\2\2)*\7G\2\2*+\7R\2\2+,\7U\2\2,\26\3\2\2\2\3\2\2")
        return buf.getvalue()


class TestLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    WHILE = 2
    CONST = 3
    CONSUMER1 = 4
    OPERATOR2 = 5
    ASSIGNMENT = 6
    IDENT = 7
    LPAR = 8
    RPAR = 9
    EPS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'a'", "'b'", "'c'", "'d'", "'e'", "'f'", "'g'", "'h'", "'k'", 
            "'EPS'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "WHILE", "CONST", "CONSUMER1", "OPERATOR2", "ASSIGNMENT", 
            "IDENT", "LPAR", "RPAR", "EPS" ]

    ruleNames = [ "IF", "WHILE", "CONST", "CONSUMER1", "OPERATOR2", "ASSIGNMENT", 
                  "IDENT", "LPAR", "RPAR", "EPS" ]

    grammarFileName = "Test.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


