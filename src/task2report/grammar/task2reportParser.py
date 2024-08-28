# Generated from grammar/task2report.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,1,0,1,1,1,
        1,1,1,1,1,1,2,1,2,1,3,3,3,34,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,3,6,45,8,6,1,6,3,6,48,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,0,
        0,9,0,2,4,6,8,10,12,14,16,0,0,52,0,20,1,0,0,0,2,26,1,0,0,0,4,30,
        1,0,0,0,6,33,1,0,0,0,8,35,1,0,0,0,10,37,1,0,0,0,12,39,1,0,0,0,14,
        51,1,0,0,0,16,53,1,0,0,0,18,21,3,2,1,0,19,21,3,12,6,0,20,18,1,0,
        0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,
        1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,5,1,0,0,27,28,3,4,2,0,28,
        29,5,4,0,0,29,3,1,0,0,0,30,31,5,3,0,0,31,5,1,0,0,0,32,34,5,5,0,0,
        33,32,1,0,0,0,33,34,1,0,0,0,34,7,1,0,0,0,35,36,5,10,0,0,36,9,1,0,
        0,0,37,38,5,6,0,0,38,11,1,0,0,0,39,40,6,6,-1,0,40,41,3,6,3,0,41,
        42,3,10,5,0,42,44,3,4,2,0,43,45,3,8,4,0,44,43,1,0,0,0,44,45,1,0,
        0,0,45,47,1,0,0,0,46,48,3,16,8,0,47,46,1,0,0,0,47,48,1,0,0,0,48,
        49,1,0,0,0,49,50,5,4,0,0,50,13,1,0,0,0,51,52,5,3,0,0,52,15,1,0,0,
        0,53,54,5,2,0,0,54,55,3,14,7,0,55,17,1,0,0,0,5,20,22,33,44,47
    ]

class task2reportParser ( Parser ):

    grammarFileName = "task2report.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'# '", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WORDS", "EOL", 
                      "SPACES", "STAR", "YEAR", "MONTH", "DAY", "DATE" ]

    RULE_top = 0
    RULE_heading = 1
    RULE_string = 2
    RULE_indent = 3
    RULE_date = 4
    RULE_star = 5
    RULE_bullet = 6
    RULE_hex = 7
    RULE_tag = 8

    ruleNames =  [ "top", "heading", "string", "indent", "date", "star", 
                   "bullet", "hex", "tag" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WORDS=3
    EOL=4
    SPACES=5
    STAR=6
    YEAR=7
    MONTH=8
    DAY=9
    DATE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(task2reportParser.EOF, 0)

        def heading(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(task2reportParser.HeadingContext)
            else:
                return self.getTypedRuleContext(task2reportParser.HeadingContext,i)


        def bullet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(task2reportParser.BulletContext)
            else:
                return self.getTypedRuleContext(task2reportParser.BulletContext,i)


        def getRuleIndex(self):
            return task2reportParser.RULE_top

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop" ):
                listener.enterTop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop" ):
                listener.exitTop(self)




    def top(self):

        localctx = task2reportParser.TopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_top)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 18
                    self.heading()
                    pass
                elif token in [5, 6]:
                    self.state = 19
                    self.bullet()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 98) != 0)):
                    break

            self.state = 24
            self.match(task2reportParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(task2reportParser.StringContext,0)


        def EOL(self):
            return self.getToken(task2reportParser.EOL, 0)

        def getRuleIndex(self):
            return task2reportParser.RULE_heading

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading" ):
                listener.enterHeading(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading" ):
                listener.exitHeading(self)




    def heading(self):

        localctx = task2reportParser.HeadingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_heading)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(task2reportParser.T__0)
            self.state = 27
            self.string()
            self.state = 28
            self.match(task2reportParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORDS(self):
            return self.getToken(task2reportParser.WORDS, 0)

        def getRuleIndex(self):
            return task2reportParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = task2reportParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(task2reportParser.WORDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACES(self):
            return self.getToken(task2reportParser.SPACES, 0)

        def getRuleIndex(self):
            return task2reportParser.RULE_indent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndent" ):
                listener.enterIndent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndent" ):
                listener.exitIndent(self)




    def indent(self):

        localctx = task2reportParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 32
                self.match(task2reportParser.SPACES)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(task2reportParser.DATE, 0)

        def getRuleIndex(self):
            return task2reportParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)




    def date(self):

        localctx = task2reportParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(task2reportParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(task2reportParser.STAR, 0)

        def getRuleIndex(self):
            return task2reportParser.RULE_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar" ):
                listener.enterStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar" ):
                listener.exitStar(self)




    def star(self):

        localctx = task2reportParser.StarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_star)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(task2reportParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BulletContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indent(self):
            return self.getTypedRuleContext(task2reportParser.IndentContext,0)


        def star(self):
            return self.getTypedRuleContext(task2reportParser.StarContext,0)


        def string(self):
            return self.getTypedRuleContext(task2reportParser.StringContext,0)


        def EOL(self):
            return self.getToken(task2reportParser.EOL, 0)

        def date(self):
            return self.getTypedRuleContext(task2reportParser.DateContext,0)


        def tag(self):
            return self.getTypedRuleContext(task2reportParser.TagContext,0)


        def getRuleIndex(self):
            return task2reportParser.RULE_bullet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBullet" ):
                listener.enterBullet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBullet" ):
                listener.exitBullet(self)




    def bullet(self):

        localctx = task2reportParser.BulletContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bullet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            this.column==0
            self.state = 40
            self.indent()
            self.state = 41
            self.star()
            self.state = 42
            self.string()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 43
                self.date()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 46
                self.tag()


            self.state = 49
            self.match(task2reportParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORDS(self):
            return self.getToken(task2reportParser.WORDS, 0)

        def getRuleIndex(self):
            return task2reportParser.RULE_hex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex" ):
                listener.enterHex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex" ):
                listener.exitHex(self)




    def hex_(self):

        localctx = task2reportParser.HexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_hex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(task2reportParser.WORDS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hex_(self):
            return self.getTypedRuleContext(task2reportParser.HexContext,0)


        def getRuleIndex(self):
            return task2reportParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = task2reportParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(task2reportParser.T__1)
            self.state = 54
            self.hex_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





