# Generated from ../src/Main.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MainParser import MainParser
else:
    from MainParser import MainParser

# This class defines a complete generic visitor for a parse tree produced by MainParser.

class MainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MainParser#start.
    def visitStart(self, ctx:MainParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#init.
    def visitInit(self, ctx:MainParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#lexingRule.
    def visitLexingRule(self, ctx:MainParser.LexingRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#parsingRule.
    def visitParsingRule(self, ctx:MainParser.ParsingRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#parsingExpr.
    def visitParsingExpr(self, ctx:MainParser.ParsingExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#parsingSolo.
    def visitParsingSolo(self, ctx:MainParser.ParsingSoloContext):
        return self.visitChildren(ctx)



del MainParser