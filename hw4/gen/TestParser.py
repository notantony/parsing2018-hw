# Generated from ../src/Test.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3)\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\5\6\62\n\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bA\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r^\n\r\3\16\3\16\3\16\3\17\3\17\3\17\2\2\20")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2a\2\36\3\2\2")
        buf.write("\2\4(\3\2\2\2\6*\3\2\2\2\b,\3\2\2\2\n\61\3\2\2\2\f\63")
        buf.write("\3\2\2\2\16@\3\2\2\2\20B\3\2\2\2\22F\3\2\2\2\24J\3\2\2")
        buf.write("\2\26O\3\2\2\2\30]\3\2\2\2\32_\3\2\2\2\34b\3\2\2\2\36")
        buf.write("\37\5\6\4\2\37 \5\b\5\2 !\7\b\2\2!\"\5\16\b\2\"#\5\4\3")
        buf.write("\2#\3\3\2\2\2$%\5\16\b\2%&\5\4\3\2&)\3\2\2\2\')\5\16\b")
        buf.write("\2($\3\2\2\2(\'\3\2\2\2)\5\3\2\2\2*+\7\t\2\2+\7\3\2\2")
        buf.write("\2,-\5\n\6\2-\t\3\2\2\2./\7\t\2\2/\62\5\n\6\2\60\62\7")
        buf.write("\f\2\2\61.\3\2\2\2\61\60\3\2\2\2\62\13\3\2\2\2\63\64\5")
        buf.write("\16\b\2\64\65\5\4\3\2\65\r\3\2\2\2\66A\5\24\13\2\67A\5")
        buf.write("\20\t\28A\5\22\n\29A\5\26\f\2:A\5\30\r\2;<\7\n\2\2<=\5")
        buf.write("\f\7\2=>\7\13\2\2>A\3\2\2\2?A\5\32\16\2@\66\3\2\2\2@\67")
        buf.write("\3\2\2\2@8\3\2\2\2@9\3\2\2\2@:\3\2\2\2@;\3\2\2\2@?\3\2")
        buf.write("\2\2A\17\3\2\2\2BC\7\3\2\2CD\5\30\r\2DE\5\16\b\2E\21\3")
        buf.write("\2\2\2FG\7\4\2\2GH\5\30\r\2HI\5\16\b\2I\23\3\2\2\2JK\7")
        buf.write("\3\2\2KL\5\30\r\2LM\5\16\b\2MN\5\16\b\2N\25\3\2\2\2OP")
        buf.write("\7\b\2\2PQ\7\t\2\2QR\5\30\r\2R\27\3\2\2\2S^\7\5\2\2TU")
        buf.write("\7\7\2\2UV\5\30\r\2VW\5\30\r\2W^\3\2\2\2X^\7\t\2\2YZ\7")
        buf.write("\n\2\2Z[\5\30\r\2[\\\7\13\2\2\\^\3\2\2\2]S\3\2\2\2]T\3")
        buf.write("\2\2\2]X\3\2\2\2]Y\3\2\2\2^\31\3\2\2\2_`\7\6\2\2`a\5\30")
        buf.write("\r\2a\33\3\2\2\2bc\7\f\2\2c\35\3\2\2\2\6(\61@]")
        return buf.getvalue()


class TestParser ( Parser ):

    grammarFileName = "Test.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'", "'d'", "'e'", "'f'", 
                     "'g'", "'h'", "'k'", "'EPS'" ]

    symbolicNames = [ "<INVALID>", "IF", "WHILE", "CONST", "CONSUMER1", 
                      "OPERATOR2", "ASSIGNMENT", "IDENT", "LPAR", "RPAR", 
                      "EPS" ]

    RULE_start = 0
    RULE_statements = 1
    RULE_name = 2
    RULE_vars = 3
    RULE_idents = 4
    RULE_program = 5
    RULE_statement = 6
    RULE_ifSingle = 7
    RULE_whileC = 8
    RULE_ifElse = 9
    RULE_assignment = 10
    RULE_expr = 11
    RULE_action = 12
    RULE_eps = 13

    ruleNames =  [ "start", "statements", "name", "vars", "idents", "program", 
                   "statement", "ifSingle", "whileC", "ifElse", "assignment", 
                   "expr", "action", "eps" ]

    EOF = Token.EOF
    IF=1
    WHILE=2
    CONST=3
    CONSUMER1=4
    OPERATOR2=5
    ASSIGNMENT=6
    IDENT=7
    LPAR=8
    RPAR=9
    EPS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(TestParser.NameContext,0)


        def vars(self):
            return self.getTypedRuleContext(TestParser.VarsContext,0)


        def ASSIGNMENT(self):
            return self.getToken(TestParser.ASSIGNMENT, 0)

        def statement(self):
            return self.getTypedRuleContext(TestParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(TestParser.StatementsContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = TestParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.name()
            self.state = 29
            self.vars()
            self.state = 30
            self.match(TestParser.ASSIGNMENT)
            self.state = 31
            self.statement()
            self.state = 32
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(TestParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(TestParser.StatementsContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = TestParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.statement()
                self.state = 35
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(TestParser.IDENT, 0)

        def getRuleIndex(self):
            return TestParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = TestParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(TestParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idents(self):
            return self.getTypedRuleContext(TestParser.IdentsContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars(self):

        localctx = TestParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.idents()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(TestParser.IDENT, 0)

        def idents(self):
            return self.getTypedRuleContext(TestParser.IdentsContext,0)


        def EPS(self):
            return self.getToken(TestParser.EPS, 0)

        def getRuleIndex(self):
            return TestParser.RULE_idents

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdents" ):
                listener.enterIdents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdents" ):
                listener.exitIdents(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdents" ):
                return visitor.visitIdents(self)
            else:
                return visitor.visitChildren(self)




    def idents(self):

        localctx = TestParser.IdentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idents)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TestParser.IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(TestParser.IDENT)
                self.state = 45
                self.idents()
                pass
            elif token in [TestParser.EPS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(TestParser.EPS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(TestParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(TestParser.StatementsContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TestParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.statement()
            self.state = 50
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElse(self):
            return self.getTypedRuleContext(TestParser.IfElseContext,0)


        def ifSingle(self):
            return self.getTypedRuleContext(TestParser.IfSingleContext,0)


        def whileC(self):
            return self.getTypedRuleContext(TestParser.WhileCContext,0)


        def assignment(self):
            return self.getTypedRuleContext(TestParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(TestParser.ExprContext,0)


        def LPAR(self):
            return self.getToken(TestParser.LPAR, 0)

        def program(self):
            return self.getTypedRuleContext(TestParser.ProgramContext,0)


        def RPAR(self):
            return self.getToken(TestParser.RPAR, 0)

        def action(self):
            return self.getTypedRuleContext(TestParser.ActionContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TestParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.ifElse()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.ifSingle()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.whileC()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.assignment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(TestParser.LPAR)
                self.state = 58
                self.program()
                self.state = 59
                self.match(TestParser.RPAR)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.action()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfSingleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TestParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(TestParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(TestParser.StatementContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_ifSingle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfSingle" ):
                listener.enterIfSingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfSingle" ):
                listener.exitIfSingle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfSingle" ):
                return visitor.visitIfSingle(self)
            else:
                return visitor.visitChildren(self)




    def ifSingle(self):

        localctx = TestParser.IfSingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifSingle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(TestParser.IF)
            self.state = 65
            self.expr()
            self.state = 66
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileCContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TestParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(TestParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(TestParser.StatementContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_whileC

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileC" ):
                listener.enterWhileC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileC" ):
                listener.exitWhileC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileC" ):
                return visitor.visitWhileC(self)
            else:
                return visitor.visitChildren(self)




    def whileC(self):

        localctx = TestParser.WhileCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(TestParser.WHILE)
            self.state = 69
            self.expr()
            self.state = 70
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TestParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(TestParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TestParser.StatementContext)
            else:
                return self.getTypedRuleContext(TestParser.StatementContext,i)


        def getRuleIndex(self):
            return TestParser.RULE_ifElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)




    def ifElse(self):

        localctx = TestParser.IfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(TestParser.IF)
            self.state = 73
            self.expr()
            self.state = 74
            self.statement()
            self.state = 75
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(TestParser.ASSIGNMENT, 0)

        def IDENT(self):
            return self.getToken(TestParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(TestParser.ExprContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = TestParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(TestParser.ASSIGNMENT)
            self.state = 78
            self.match(TestParser.IDENT)
            self.state = 79
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(TestParser.CONST, 0)

        def OPERATOR2(self):
            return self.getToken(TestParser.OPERATOR2, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TestParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestParser.ExprContext,i)


        def IDENT(self):
            return self.getToken(TestParser.IDENT, 0)

        def LPAR(self):
            return self.getToken(TestParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(TestParser.RPAR, 0)

        def getRuleIndex(self):
            return TestParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = TestParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TestParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(TestParser.CONST)
                pass
            elif token in [TestParser.OPERATOR2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(TestParser.OPERATOR2)
                self.state = 83
                self.expr()
                self.state = 84
                self.expr()
                pass
            elif token in [TestParser.IDENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(TestParser.IDENT)
                pass
            elif token in [TestParser.LPAR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.match(TestParser.LPAR)
                self.state = 88
                self.expr()
                self.state = 89
                self.match(TestParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSUMER1(self):
            return self.getToken(TestParser.CONSUMER1, 0)

        def expr(self):
            return self.getTypedRuleContext(TestParser.ExprContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = TestParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TestParser.CONSUMER1)
            self.state = 94
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EpsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EPS(self):
            return self.getToken(TestParser.EPS, 0)

        def getRuleIndex(self):
            return TestParser.RULE_eps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEps" ):
                listener.enterEps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEps" ):
                listener.exitEps(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEps" ):
                return visitor.visitEps(self)
            else:
                return visitor.visitChildren(self)




    def eps(self):

        localctx = TestParser.EpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eps)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(TestParser.EPS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





