# Generated from ../src/Main.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\5\2\26\n\2\3\2\7\2\31")
        buf.write("\n\2\f\2\16\2\34\13\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\5\5)\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\64\n\6\5\6\66\n\6\3\6\3\6\3\6\7\6;\n\6\f\6\16")
        buf.write("\6>\13\6\3\7\3\7\5\7B\n\7\3\7\3\7\5\7F\n\7\5\7H\n\7\3")
        buf.write("\7\2\3\n\b\2\4\6\b\n\f\2\2\2M\2\21\3\2\2\2\4\35\3\2\2")
        buf.write("\2\6\37\3\2\2\2\b$\3\2\2\2\n\65\3\2\2\2\fG\3\2\2\2\16")
        buf.write("\20\5\6\4\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2")
        buf.write("\21\22\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\24\26\5\4\3")
        buf.write("\2\25\24\3\2\2\2\25\26\3\2\2\2\26\32\3\2\2\2\27\31\5\b")
        buf.write("\5\2\30\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3")
        buf.write("\2\2\2\33\3\3\2\2\2\34\32\3\2\2\2\35\36\7\3\2\2\36\5\3")
        buf.write("\2\2\2\37 \7\7\2\2 !\7\n\2\2!\"\7\4\2\2\"#\7\13\2\2#\7")
        buf.write("\3\2\2\2$%\7\6\2\2%&\7\n\2\2&(\5\n\6\2\')\7\3\2\2(\'\3")
        buf.write("\2\2\2()\3\2\2\2)*\3\2\2\2*+\7\13\2\2+\t\3\2\2\2,-\b\6")
        buf.write("\1\2-.\7\b\2\2./\5\n\6\2/\60\7\t\2\2\60\66\3\2\2\2\61")
        buf.write("\63\5\f\7\2\62\64\5\n\6\2\63\62\3\2\2\2\63\64\3\2\2\2")
        buf.write("\64\66\3\2\2\2\65,\3\2\2\2\65\61\3\2\2\2\66<\3\2\2\2\67")
        buf.write("8\f\4\2\289\7\r\2\29;\5\n\6\5:\67\3\2\2\2;>\3\2\2\2<:")
        buf.write("\3\2\2\2<=\3\2\2\2=\13\3\2\2\2><\3\2\2\2?A\7\6\2\2@B\7")
        buf.write("\20\2\2A@\3\2\2\2AB\3\2\2\2BH\3\2\2\2CE\7\7\2\2DF\7\20")
        buf.write("\2\2ED\3\2\2\2EF\3\2\2\2FH\3\2\2\2G?\3\2\2\2GC\3\2\2\2")
        buf.write("H\r\3\2\2\2\f\21\25\32(\63\65<AEG")
        return buf.getvalue()


class MainParser ( Parser ):

    grammarFileName = "Main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "':'", "';'", 
                     "'->'", "'|'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "CODE", "REGEXP", "WHITESPACE", "LOWER_IDENT", 
                      "CAPS_IDENT", "LPAR", "RPAR", "COLON", "SEMICOLON", 
                      "ARROW", "BAR", "DOT", "EQ", "AT" ]

    RULE_start = 0
    RULE_init = 1
    RULE_lexingRule = 2
    RULE_parsingRule = 3
    RULE_parsingExpr = 4
    RULE_parsingSolo = 5

    ruleNames =  [ "start", "init", "lexingRule", "parsingRule", "parsingExpr", 
                   "parsingSolo" ]

    EOF = Token.EOF
    CODE=1
    REGEXP=2
    WHITESPACE=3
    LOWER_IDENT=4
    CAPS_IDENT=5
    LPAR=6
    RPAR=7
    COLON=8
    SEMICOLON=9
    ARROW=10
    BAR=11
    DOT=12
    EQ=13
    AT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexingRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MainParser.LexingRuleContext)
            else:
                return self.getTypedRuleContext(MainParser.LexingRuleContext,i)


        def init(self):
            return self.getTypedRuleContext(MainParser.InitContext,0)


        def parsingRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MainParser.ParsingRuleContext)
            else:
                return self.getTypedRuleContext(MainParser.ParsingRuleContext,i)


        def getRuleIndex(self):
            return MainParser.RULE_start

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

        localctx = MainParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MainParser.CAPS_IDENT:
                self.state = 12
                self.lexingRule()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MainParser.CODE:
                self.state = 18
                self.init()


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MainParser.LOWER_IDENT:
                self.state = 21
                self.parsingRule()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE(self):
            return self.getToken(MainParser.CODE, 0)

        def getRuleIndex(self):
            return MainParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MainParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(MainParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexingRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAPS_IDENT(self):
            return self.getToken(MainParser.CAPS_IDENT, 0)

        def COLON(self):
            return self.getToken(MainParser.COLON, 0)

        def REGEXP(self):
            return self.getToken(MainParser.REGEXP, 0)

        def SEMICOLON(self):
            return self.getToken(MainParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MainParser.RULE_lexingRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexingRule" ):
                listener.enterLexingRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexingRule" ):
                listener.exitLexingRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexingRule" ):
                return visitor.visitLexingRule(self)
            else:
                return visitor.visitChildren(self)




    def lexingRule(self):

        localctx = MainParser.LexingRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lexingRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MainParser.CAPS_IDENT)
            self.state = 30
            self.match(MainParser.COLON)
            self.state = 31
            self.match(MainParser.REGEXP)
            self.state = 32
            self.match(MainParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParsingRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWER_IDENT(self):
            return self.getToken(MainParser.LOWER_IDENT, 0)

        def COLON(self):
            return self.getToken(MainParser.COLON, 0)

        def parsingExpr(self):
            return self.getTypedRuleContext(MainParser.ParsingExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MainParser.SEMICOLON, 0)

        def CODE(self):
            return self.getToken(MainParser.CODE, 0)

        def getRuleIndex(self):
            return MainParser.RULE_parsingRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParsingRule" ):
                listener.enterParsingRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParsingRule" ):
                listener.exitParsingRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParsingRule" ):
                return visitor.visitParsingRule(self)
            else:
                return visitor.visitChildren(self)




    def parsingRule(self):

        localctx = MainParser.ParsingRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parsingRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MainParser.LOWER_IDENT)
            self.state = 35
            self.match(MainParser.COLON)
            self.state = 36
            self.parsingExpr(0)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MainParser.CODE:
                self.state = 37
                self.match(MainParser.CODE)


            self.state = 40
            self.match(MainParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParsingExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MainParser.LPAR, 0)

        def parsingExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MainParser.ParsingExprContext)
            else:
                return self.getTypedRuleContext(MainParser.ParsingExprContext,i)


        def RPAR(self):
            return self.getToken(MainParser.RPAR, 0)

        def parsingSolo(self):
            return self.getTypedRuleContext(MainParser.ParsingSoloContext,0)


        def BAR(self):
            return self.getToken(MainParser.BAR, 0)

        def getRuleIndex(self):
            return MainParser.RULE_parsingExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParsingExpr" ):
                listener.enterParsingExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParsingExpr" ):
                listener.exitParsingExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParsingExpr" ):
                return visitor.visitParsingExpr(self)
            else:
                return visitor.visitChildren(self)



    def parsingExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MainParser.ParsingExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_parsingExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MainParser.LPAR]:
                self.state = 43
                self.match(MainParser.LPAR)
                self.state = 44
                self.parsingExpr(0)
                self.state = 45
                self.match(MainParser.RPAR)
                pass
            elif token in [MainParser.LOWER_IDENT, MainParser.CAPS_IDENT]:
                self.state = 47
                self.parsingSolo()
                self.state = 49
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.parsingExpr(0)


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MainParser.ParsingExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parsingExpr)
                    self.state = 53
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 54
                    self.match(MainParser.BAR)
                    self.state = 55
                    self.parsingExpr(3) 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParsingSoloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWER_IDENT(self):
            return self.getToken(MainParser.LOWER_IDENT, 0)

        def AT(self):
            return self.getToken(MainParser.AT, 0)

        def CAPS_IDENT(self):
            return self.getToken(MainParser.CAPS_IDENT, 0)

        def getRuleIndex(self):
            return MainParser.RULE_parsingSolo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParsingSolo" ):
                listener.enterParsingSolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParsingSolo" ):
                listener.exitParsingSolo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParsingSolo" ):
                return visitor.visitParsingSolo(self)
            else:
                return visitor.visitChildren(self)




    def parsingSolo(self):

        localctx = MainParser.ParsingSoloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parsingSolo)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MainParser.LOWER_IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(MainParser.LOWER_IDENT)
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.match(MainParser.AT)


                pass
            elif token in [MainParser.CAPS_IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(MainParser.CAPS_IDENT)
                self.state = 67
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self.match(MainParser.AT)


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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.parsingExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def parsingExpr_sempred(self, localctx:ParsingExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




