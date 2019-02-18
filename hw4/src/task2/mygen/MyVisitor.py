class MyVisitor:
    def visitChildren(self, c):
        if c.children is not None:
            for one in c.children:
                one.visit(self)

    def visitLBRACKET(self, c):
        pass

    def visitRBRACKET(self, c):
        pass

    def visitPTR(self, c):
        pass

    def visitSEMICOLON(self, c):
        pass

    def visitCOMMA(self, c):
        pass

    def visitIDENT(self, c):
        pass

    def visitstart(self, c):
        self.visitChildren(c)

    def visittype_(self, c):
        self.visitChildren(c)

    def visitargs(self, c):
        self.visitChildren(c)

    def visitargs_(self, c):
        self.visitChildren(c)

    def visitmodifier(self, c):
        self.visitChildren(c)

