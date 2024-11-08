# Generated from Language.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete generic visitor for a parse tree produced by LanguageParser.

class LanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LanguageParser#start_.
    def visitStart_(self, ctx:LanguageParser.Start_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statement.
    def visitStatement(self, ctx:LanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#declaration.
    def visitDeclaration(self, ctx:LanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expression.
    def visitExpression(self, ctx:LanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expr.
    def visitExpr(self, ctx:LanguageParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#term.
    def visitTerm(self, ctx:LanguageParser.TermContext):
        return self.visitChildren(ctx)



del LanguageParser