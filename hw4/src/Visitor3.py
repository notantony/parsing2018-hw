from MyVisitor import MyVisitor

class Visitor3(MyVisitor):
    def __init__(self, output):
        self.output = output
        self.tabs = 0
        self.inputVars = set()
        self.localVars = set()
        self.extra = 0

    def printTabs(self):
        for i in range(self.tabs):
            self.output.write("    ")

    def printExtra(self):
        for i in range(self.extra):
            self.output.write("    ")

    def printEndl(self):
        self.output.write(";\n")

    def openContext(self):
        self.output.write("{\n")
        self.tabs += 1

    def closeContext(self):
        self.tabs -= 1
        self.printTabs()
        self.output.write("}\n")

    def writeVars(self, start):
        t = self
        class varsVisitor(MyVisitor):
            def visitassignment(self, c):
                var = c.IDENT
                if var not in t.inputVars and var not in t.localVars:
                    t.localVars.add(var)

        for one in start.sts:
            one.visit(varsVisitor())

        if len(self.localVars) > 0:
            self.printTabs()
            self.output.write("int {};\n".format(", ".join(self.localVars)))

    def visitChildren(self, c):
        if c.children is not None:
            for one in c.children:
                one.visit(self)


    def visitstart(self, c):
        self.output.write("void ")
        self.output.write(c.name)
        for var in c.vars:
            self.inputVars.add(var)
        self.output.write("({}) ".format(", ".join(map(lambda x: "int "+ x, c.vars))))
        self.openContext()
        self.writeVars(c)
        for one in c.sts:
            one.visit(self)
        self.closeContext()

    def visitstatement(self, c):
        if hasattr(c, "sts"):
            self.printTabs()
            self.openContext()
            for one in c.sts:
                one.visit(self)
            self.closeContext()
        else:
            self.visitChildren(c)

    def visitifC(self, c):
        self.printTabs()
        self.output.write(c.COND)
        self.output.write("\n")
        if not hasattr(c.stat, "sts"):
            self.extra += 1
            self.printExtra()
        c.stat.visit(self)
        self.extra -= 1
        if c.post.post is not None:
            self.printTabs()
            self.output.write("else ")
            self.output.write("\n")
            if not hasattr(c.post.post, "sts"):
                self.extra += 1
                self.printExtra()
            c.post.post.visit(self)
            self.extra -= 1

    def visitifPost(self, c):
        self.visitChildren(c)

    def visitwhileC(self, c):
        self.printTabs()
        self.output.write(c.COND)
        self.output.write("\n")
        if not hasattr(c.stat, "sts"):
            self.extra += 1
            self.printExtra()
        c.stat.visit(self)
        self.extra -= 1

    def visitassignment(self, c):
        self.printTabs()
        self.output.write(c.STR)
        self.printEndl()

    def visitexpr(self, c):
        self.output.write(c.STR)

    def visitaction(self, c):
        self.printTabs()
        self.output.write(c.STR)
        self.printEndl()

    def visitCONST(self, c):
        print(c.data)

    def visitCONSUMER1(self, c):
        print(c.data)

    def visitASSIGNMENT(self, c):
        print(c.data)

    def visitIDENT(self, c):
        print(c.data)