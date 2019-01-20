import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.HashMap;
import java.util.HashSet;

public class MyVisitor extends MainBaseVisitor<Void> {
    private int tabs = 0;
    private StringBuilder output = new StringBuilder();
    private HashSet<String> inputVars = new HashSet<>();
    private HashSet<String> localVars = new HashSet<>();

    private void printTabs() {
        for (int i = 0; i < 4 * tabs; i++) output.append(' ');
    }

    private void printEndl() {
        output.append(";\n");
    }

    private void openContext() {
        output.append("{\n");
        tabs++;
    }

    private void closeContext() {
        tabs--;
        printTabs();
        output.append("}\n");
    }

    private void writeVars(MainParser.StartContext ctx) {
        MainBaseVisitor<Void> varsVisitor = new MainBaseVisitor<>() {
            @Override
            public Void visitAssignment(MainParser.AssignmentContext ctx) {
                String var = ctx.IDENT().getText();
                if (!inputVars.contains(var) && !localVars.contains(var)) {
                    localVars.add(var);
                }
                return super.visitAssignment(ctx);
            }
        };
        for (MainParser.StatementContext one: ctx.statement()){
            varsVisitor.visit(one);
        }

        boolean flag = false;
        if (!localVars.isEmpty()) {
            printTabs();
            output.append("int ");
            for (String var : localVars) {
                if (!flag) {
                    flag = true;
                } else {
                    output.append(", ");
                }
                output.append(var);
            }
            printEndl();
        }
    }

    public String getOutput() {
        return output.toString();
    }

    @Override
    public Void visitStart(MainParser.StartContext ctx) {
        output.append("void ");
        visit(ctx.name());
        visit(ctx.vars());
        openContext();
        writeVars(ctx);
        for (MainParser.StatementContext one: ctx.statement()) {
            visit(one);
        }
        closeContext();
        return null;
    }

    @Override
    public Void visitVars(MainParser.VarsContext ctx) {
        boolean flag = false;
        output.append('(');
        for (ParseTree var : ctx.IDENT()) {
            if (!flag) {
                flag = true;
            } else {
                output.append(", ");
            }
            inputVars.add(var.getText());
            output.append("int ");
            output.append(var);
        }
        output.append(") ");
        return null;
    }

    @Override
    public Void visitProgram(MainParser.ProgramContext ctx) {
        tabs--;
        printTabs();
        if (ctx.children.size() > 1) {
            tabs--;
            openContext();
            tabs++;
        }
        visitChildren(ctx);
        if (ctx.children.size() > 1) {
            closeContext();
        }
        return null;

    }

    @Override
    public Void visitAssignmentStatement(MainParser.AssignmentStatementContext ctx) {
        printTabs();
        visit(ctx.assignment());
        printEndl();
        return null;
    }

    @Override
    public Void visitExprStatement(MainParser.ExprStatementContext ctx) {
        printTabs();
        visitChildren(ctx);
        printEndl();
        return null;
    }

    @Override
    public Void visitProgramStatement(MainParser.ProgramStatementContext ctx) {
        visit(ctx.program());
        return null;
    }

    @Override
    public Void visitActionStatement(MainParser.ActionStatementContext ctx) {
        printTabs();
        visit(ctx.action());
        printEndl();
        return null;
    }

    @Override
    public Void visitWhileC(MainParser.WhileCContext ctx) {
        printTabs();
        output.append("while (");;
        visit(ctx.expr());
        output.append(")\n");
        tabs++;
        visit(ctx.statement());
        tabs--;
        return null;
    }

    @Override
    public Void visitIfSingle(MainParser.IfSingleContext ctx) {
        printTabs();
        output.append("if (");
        visit(ctx.expr());
        output.append(")\n");
        tabs++;
        visit(ctx.statement());
        tabs--;
        return null;
    }



    @Override
    public Void visitIfElse(MainParser.IfElseContext ctx) {
        printTabs();
        output.append("if (");
        visit(ctx.expr());
        output.append(") ");
        openContext();
        visit(ctx.statement(0));
        closeContext();
        printTabs();
        output.append("else ");
        openContext();
        visit(ctx.statement(1));
        closeContext();
        return null;
    }

    @Override
    public Void visitAssignment(MainParser.AssignmentContext ctx) {
        visit(ctx.IDENT());
        output.append(" = ");
        visit(ctx.expr());
        return null;
    }

    @Override
    public Void visitExpr(MainParser.ExprContext ctx) {
        if (ctx.expr().size() == 2) {
            output.append('(');
            visit(ctx.expr(0));
            output.append(" ");
            visit(ctx.OPERATOR2());
            output.append(" ");
            visit(ctx.expr(1));
            output.append(')');
        } else if (ctx.expr().size() == 1) {
            output.append('(');
            visit(ctx.expr(0));
            output.append(')');
        } else {
            visitChildren(ctx);
        }
        return null;
    }

    @Override
    public Void visitAction(MainParser.ActionContext ctx) {
        output.append("std::cout << ");
        visit(ctx.expr());
        return null;
    }

    @Override
    public Void visitTerminal(TerminalNode node) {
        output.append(node.toString());
        return null;
    }

    @Override
    public Void visitErrorNode(ErrorNode node) {
        return null;
    }
}
