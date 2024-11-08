# Generated from Language.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):

    # Enter a parse tree produced by LanguageParser#start_.
    def enterStart_(self, ctx:LanguageParser.Start_Context):
        pass

    # Exit a parse tree produced by LanguageParser#start_.
    def exitStart_(self, ctx:LanguageParser.Start_Context):
        pass


    # Enter a parse tree produced by LanguageParser#statement.
    def enterStatement(self, ctx:LanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#statement.
    def exitStatement(self, ctx:LanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#declaration.
    def enterDeclaration(self, ctx:LanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by LanguageParser#declaration.
    def exitDeclaration(self, ctx:LanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by LanguageParser#expression.
    def enterExpression(self, ctx:LanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LanguageParser#expression.
    def exitExpression(self, ctx:LanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LanguageParser#expr.
    def enterExpr(self, ctx:LanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr.
    def exitExpr(self, ctx:LanguageParser.ExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#term.
    def enterTerm(self, ctx:LanguageParser.TermContext):
        pass

    # Exit a parse tree produced by LanguageParser#term.
    def exitTerm(self, ctx:LanguageParser.TermContext):
        pass



del LanguageParser