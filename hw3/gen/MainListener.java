// Generated from C:/Users/Anton/IdeaProjects/mt2018-hw/hw3/java\Main.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MainParser}.
 */
public interface MainListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MainParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(MainParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(MainParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(MainParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(MainParser.NameContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(MainParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(MainParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MainParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MainParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifElseStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfElseStatement(MainParser.IfElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifElseStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfElseStatement(MainParser.IfElseStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifSingleStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfSingleStatement(MainParser.IfSingleStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifSingleStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfSingleStatement(MainParser.IfSingleStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(MainParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(MainParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignmentStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(MainParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignmentStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(MainParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exprStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExprStatement(MainParser.ExprStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exprStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExprStatement(MainParser.ExprStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code programStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterProgramStatement(MainParser.ProgramStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code programStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitProgramStatement(MainParser.ProgramStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code actionStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterActionStatement(MainParser.ActionStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code actionStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitActionStatement(MainParser.ActionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#ifSingle}.
	 * @param ctx the parse tree
	 */
	void enterIfSingle(MainParser.IfSingleContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#ifSingle}.
	 * @param ctx the parse tree
	 */
	void exitIfSingle(MainParser.IfSingleContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#whileC}.
	 * @param ctx the parse tree
	 */
	void enterWhileC(MainParser.WhileCContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#whileC}.
	 * @param ctx the parse tree
	 */
	void exitWhileC(MainParser.WhileCContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(MainParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(MainParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(MainParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(MainParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MainParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MainParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(MainParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(MainParser.ActionContext ctx);
}