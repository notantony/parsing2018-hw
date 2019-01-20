import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;

public class Visualizer {
    private String format(String s) {
        return s.replace("_", "\\_").replace("&", "\\&");
    }

    public void visualize(Writer w, Parser.Node t) throws IOException {
        w.write("\\documentclass[12pt, a4paper]{article}\n" +
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
                "\\graph [tree layout, grow=down, fresh nodes, level distance=0.5in, sibling distance=0.5in]\n");


        rec(w, t);

        w.write(";\n\\end{tikzpicture}\n" +
                "\\end{landscape}" +
                "\\end{document}");
    }

    private void rec(Writer w, Parser.Node t) throws IOException {
        w.write("{");
        List<Parser.Node> children = t.getChildren();
        if (children != null) {
            w.write(" \"" + format(t.getData()) + "\" [circle, draw=black]");
            w.write(" -> {\n");
            for (int i = 0; i < children.size(); i++) {
                Parser.Node one = children.get(i);
                if (one != null) {
                    if (i != 0) {
                        w.write(",");
                    }
                    rec(w, one);
                }
            }
            w.write("}");
        } else {
            if (t.getData().equals("eps")) {
                w.write("\"$ \\varepsilon $\" [rectangle, draw=blue]");
            } else {
                w.write(" \"" + format(t.getData()) + "\" [rectangle, draw=green]");
            }
        }
        w.write("");
        w.write("}");
    }
}
