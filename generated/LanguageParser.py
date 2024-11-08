# Generated from Language.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\32\n\3\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6,\n\6\f\6\16\6/\13\6\3\7\3\7\3\7")
        buf.write("\2\3\n\b\2\4\6\b\n\f\2\4\3\2\4\5\3\2\b\t\2\60\2\17\3\2")
        buf.write("\2\2\4\31\3\2\2\2\6\33\3\2\2\2\b!\3\2\2\2\n%\3\2\2\2\f")
        buf.write("\60\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2")
        buf.write("\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\24\5\6\4")
        buf.write("\2\24\25\7\3\2\2\25\32\3\2\2\2\26\27\5\b\5\2\27\30\7\3")
        buf.write("\2\2\30\32\3\2\2\2\31\23\3\2\2\2\31\26\3\2\2\2\32\5\3")
        buf.write("\2\2\2\33\34\t\2\2\2\34\37\7\b\2\2\35\36\7\6\2\2\36 \5")
        buf.write("\n\6\2\37\35\3\2\2\2\37 \3\2\2\2 \7\3\2\2\2!\"\7\b\2\2")
        buf.write("\"#\7\6\2\2#$\5\n\6\2$\t\3\2\2\2%&\b\6\1\2&\'\5\f\7\2")
        buf.write("\'-\3\2\2\2()\f\4\2\2)*\7\7\2\2*,\5\f\7\2+(\3\2\2\2,/")
        buf.write("\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\13\3\2\2\2/-\3\2\2\2\60")
        buf.write("\61\t\3\2\2\61\r\3\2\2\2\6\21\31\37-")
        return buf.getvalue()


class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'float'", "'='", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "WS", "COMMENT" ]

    RULE_start_ = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_expression = 3
    RULE_expr = 4
    RULE_term = 5

    ruleNames =  [ "start_", "statement", "declaration", "expression", "expr", 
                   "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    NUMBER=7
    WS=8
    COMMENT=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_start_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_" ):
                listener.enterStart_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_" ):
                listener.exitStart_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_" ):
                return visitor.visitStart_(self)
            else:
                return visitor.visitChildren(self)




    def start_(self):

        localctx = LanguageParser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LanguageParser.T__1) | (1 << LanguageParser.T__2) | (1 << LanguageParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(LanguageParser.DeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(LanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LanguageParser.T__1, LanguageParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.declaration()
                self.state = 18
                self.match(LanguageParser.T__0)
                pass
            elif token in [LanguageParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expression()
                self.state = 21
                self.match(LanguageParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = LanguageParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not(_la==LanguageParser.T__1 or _la==LanguageParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 26
            self.match(LanguageParser.ID)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LanguageParser.T__3:
                self.state = 27
                self.match(LanguageParser.T__3)
                self.state = 28
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(LanguageParser.ID)
            self.state = 32
            self.match(LanguageParser.T__3)
            self.state = 33
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(LanguageParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 38
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 39
                    self.match(LanguageParser.T__4)
                    self.state = 40
                    self.term() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def NUMBER(self):
            return self.getToken(LanguageParser.NUMBER, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LanguageParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==LanguageParser.ID or _la==LanguageParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




