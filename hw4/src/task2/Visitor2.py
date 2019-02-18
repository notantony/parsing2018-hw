from mygen.MyVisitor import MyVisitor

class Visitor2(MyVisitor):
    def __init__(self, output):
        self.output = output

    def format(self, s):
        return s.replace("_", "\\_").replace("&", "\\&")

    def rec(self, t):
        self.output.write("{")
        if hasattr(t, "children") and t.children is not None:
            self.output.write(" \"" + self.format(t.data) + "\" [circle, draw=black]")
            self.output.write(" -> {\n")
            flag = False
            for one in t.children:
                if flag:
                    self.output.write(",")
                else:
                    flag = True
                self.rec(one)
            self.output.write("}")
        else:
            if hasattr(t, "children"):
                self.output.write(" \"" + self.format(t.data) + "\" [circle, draw=black]")
                self.output.write("-> {\"$ \\varepsilon $\" [rectangle, draw=blue]}")
            else:
                self.output.write(" \"" + self.format(t.data) + "\" [rectangle, draw=green]")
        self.output.write("}")

    def visitstart(self, c):
        self.visitChildren(c)

        self.output.write("\\documentclass[12pt, a4paper]{article}\n" +
                "\\RequirePackage[russian]{babel}\n" +
                "\\RequirePackage[utf8]{inputenc}\n" +
                "\\usepackage{tikz}\n" +
                "\\usepackage{pdflscape}\n" +
                "\\usetikzlibrary{graphdrawing}\n" +
                "\\usetikzlibrary{graphs}\n" +
                "\\usegdlibrary{trees}\n" +
                "\\begin{document}\n" +
                "\\begin{landscape}\n" +
                "\\pagestyle{empty}\n\n" +
                "\\begin{tikzpicture}[>=stealth]\n" +
                "\\graph [tree layout, grow=down, fresh nodes, level distance=0.5in, sibling distance=0.5in]\n")
        self.rec(c)
        self.output.write(";\n\\end{tikzpicture}\n" +
                "\\end{landscape}" +
                "\\end{document}")

    def visitIDENT(self, c):
        c.data = "I: " + c.data