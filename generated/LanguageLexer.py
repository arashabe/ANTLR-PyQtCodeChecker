# Generated from Language.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("K\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\7\7(\n\7\f")
        buf.write("\7\16\7+\13\7\3\b\6\b.\n\b\r\b\16\b/\3\b\3\b\6\b\64\n")
        buf.write("\b\r\b\16\b\65\5\b8\n\b\3\t\6\t;\n\t\r\t\16\t<\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\7\nE\n\n\f\n\16\nH\13\n\3\n\3\n\2\2\13")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\7\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\4\2\f\f")
        buf.write("\17\17\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2\2\7\33\3\2\2\2")
        buf.write("\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2\2\17-\3\2\2\2\21:\3\2")
        buf.write("\2\2\23@\3\2\2\2\25\26\7=\2\2\26\4\3\2\2\2\27\30\7k\2")
        buf.write("\2\30\31\7p\2\2\31\32\7v\2\2\32\6\3\2\2\2\33\34\7h\2\2")
        buf.write("\34\35\7n\2\2\35\36\7q\2\2\36\37\7c\2\2\37 \7v\2\2 \b")
        buf.write("\3\2\2\2!\"\7?\2\2\"\n\3\2\2\2#$\7-\2\2$\f\3\2\2\2%)\t")
        buf.write("\2\2\2&(\t\3\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2")
        buf.write("\2\2*\16\3\2\2\2+)\3\2\2\2,.\t\4\2\2-,\3\2\2\2./\3\2\2")
        buf.write("\2/-\3\2\2\2/\60\3\2\2\2\60\67\3\2\2\2\61\63\7\60\2\2")
        buf.write("\62\64\t\4\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2")
        buf.write("\2\65\66\3\2\2\2\668\3\2\2\2\67\61\3\2\2\2\678\3\2\2\2")
        buf.write("8\20\3\2\2\29;\t\5\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<")
        buf.write("=\3\2\2\2=>\3\2\2\2>?\b\t\2\2?\22\3\2\2\2@A\7\61\2\2A")
        buf.write("B\7\61\2\2BF\3\2\2\2CE\n\6\2\2DC\3\2\2\2EH\3\2\2\2FD\3")
        buf.write("\2\2\2FG\3\2\2\2GI\3\2\2\2HF\3\2\2\2IJ\b\n\2\2J\24\3\2")
        buf.write("\2\2\t\2)/\65\67<F\3\b\2\2")
        return buf.getvalue()


class LanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    ID = 6
    NUMBER = 7
    WS = 8
    COMMENT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'int'", "'float'", "'='", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "ID", "NUMBER", 
                  "WS", "COMMENT" ]

    grammarFileName = "Language.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


