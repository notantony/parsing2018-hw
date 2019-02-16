from MainVisitor import MainVisitor
from MainParser import MainParser

class LexerVisitor(MainVisitor):
    def __init__(self, output):
        self.output = output
        self.tokens = ['EOF']

    def visitStart(self, ctx: MainParser.StartContext):
        for rule in ctx.lexingRule():
            self.visit(rule)
        self.output.write("tokens = [{}]\n\n".format(", ".join(self.tokens)))
        return self.tokens

    def visitLexingRule(self, ctx: MainParser.LexingRuleContext):
        self.output.write("class {}(term):\n    regexp = r{}\n    def __init__(self, data, pos):\n        self.data = data\n        self.pos = pos\n\n".format(ctx.CAPS_IDENT().getText(), ctx.REGEXP().getText()))
        self.tokens.append(ctx.CAPS_IDENT().getText())
