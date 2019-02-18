class MyVisitor:
    def visitChildren(self, c):
        if c.children is not None:
            for one in c.children:
                one.visit(self)

    def visitIF(self, c):
        pass

    def visitWHILE(self, c):
        pass

    def visitCONST(self, c):
        pass

    def visitCONSUMER1(self, c):
        pass

    def visitOPERATOR2(self, c):
        pass

    def visitASSIGNMENT(self, c):
        pass

    def visitIDENT(self, c):
        pass

    def visitLPAR(self, c):
        pass

    def visitRPAR(self, c):
        pass

    def visitstart(self, c):
        self.visitChildren(c)

    def visitstatements(self, c):
        self.visitChildren(c)

    def visitidents(self, c):
        self.visitChildren(c)

    def visitstatement(self, c):
        self.visitChildren(c)

    def visitifC(self, c):
        self.visitChildren(c)

    def visitifPost(self, c):
        self.visitChildren(c)

    def visitwhileC(self, c):
        self.visitChildren(c)

    def visitassignment(self, c):
        self.visitChildren(c)

    def visitexpr(self, c):
        self.visitChildren(c)

    def visitaction(self, c):
        self.visitChildren(c)

