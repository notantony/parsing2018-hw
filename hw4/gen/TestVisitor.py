# Generated from ../src/Test.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete generic visitor for a parse tree produced by TestParser.

class TestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestParser#start.
    def visitStart(self, ctx:TestParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#statements.
    def visitStatements(self, ctx:TestParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#name.
    def visitName(self, ctx:TestParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#vars.
    def visitVars(self, ctx:TestParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#idents.
    def visitIdents(self, ctx:TestParser.IdentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#program.
    def visitProgram(self, ctx:TestParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#statement.
    def visitStatement(self, ctx:TestParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#ifSingle.
    def visitIfSingle(self, ctx:TestParser.IfSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#whileC.
    def visitWhileC(self, ctx:TestParser.WhileCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#ifElse.
    def visitIfElse(self, ctx:TestParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#assignment.
    def visitAssignment(self, ctx:TestParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#expr.
    def visitExpr(self, ctx:TestParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#action.
    def visitAction(self, ctx:TestParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#eps.
    def visitEps(self, ctx:TestParser.EpsContext):
        return self.visitChildren(ctx)



del TestParser