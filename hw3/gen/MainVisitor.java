// Generated from C:/Users/Anton/IdeaProjects/mt2018-hw/hw3/java\Main.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MainParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MainVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MainParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(MainParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#name}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitName(MainParser.NameContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#vars}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVars(MainParser.VarsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MainParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ifElseStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfElseStatement(MainParser.IfElseStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ifSingleStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfSingleStatement(MainParser.IfSingleStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatement(MainParser.WhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code assignmentStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentStatement(MainParser.AssignmentStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code exprStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprStatement(MainParser.ExprStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code programStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgramStatement(MainParser.ProgramStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code actionStatement}
	 * labeled alternative in {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitActionStatement(MainParser.ActionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#ifSingle}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfSingle(MainParser.IfSingleContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#whileC}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileC(MainParser.WhileCContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#ifElse}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfElse(MainParser.IfElseContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(MainParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(MainParser.ExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#action}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAction(MainParser.ActionContext ctx);
}