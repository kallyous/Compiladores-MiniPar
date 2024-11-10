# Generated from MiniPar.g4 by ANTLR 4.13.2
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
        4,1,29,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        5,2,44,8,2,10,2,12,2,47,9,2,1,2,1,2,1,3,1,3,1,3,5,3,54,8,3,10,3,
        12,3,57,9,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,65,8,4,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,78,8,6,10,6,12,6,81,9,6,1,6,1,6,3,
        6,85,8,6,1,7,1,7,1,7,5,7,90,8,7,10,7,12,7,93,9,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,5,8,103,8,8,10,8,12,8,106,9,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,123,8,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,134,8,10,10,10,12,
        10,137,9,10,1,10,0,1,20,11,0,2,4,6,8,10,12,14,16,18,20,0,3,1,0,11,
        12,1,0,13,14,1,0,15,20,143,0,22,1,0,0,0,2,32,1,0,0,0,4,40,1,0,0,
        0,6,50,1,0,0,0,8,64,1,0,0,0,10,66,1,0,0,0,12,71,1,0,0,0,14,86,1,
        0,0,0,16,96,1,0,0,0,18,109,1,0,0,0,20,122,1,0,0,0,22,27,3,2,1,0,
        23,26,3,4,2,0,24,26,3,6,3,0,25,23,1,0,0,0,25,24,1,0,0,0,26,29,1,
        0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,
        31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,34,5,2,0,0,34,35,5,27,0,
        0,35,36,5,3,0,0,36,37,5,29,0,0,37,38,5,4,0,0,38,39,5,5,0,0,39,3,
        1,0,0,0,40,41,5,6,0,0,41,45,5,7,0,0,42,44,3,8,4,0,43,42,1,0,0,0,
        44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,
        0,0,0,48,49,5,8,0,0,49,5,1,0,0,0,50,51,5,9,0,0,51,55,5,7,0,0,52,
        54,3,8,4,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,
        0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,8,0,0,59,7,1,0,0,0,60,65,3,
        10,5,0,61,65,3,12,6,0,62,65,3,16,8,0,63,65,3,18,9,0,64,60,1,0,0,
        0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,9,1,0,0,0,66,67,5,
        27,0,0,67,68,5,10,0,0,68,69,3,20,10,0,69,70,5,5,0,0,70,11,1,0,0,
        0,71,72,5,21,0,0,72,73,5,2,0,0,73,74,3,20,10,0,74,75,5,4,0,0,75,
        79,5,7,0,0,76,78,3,8,4,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,
        0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,84,5,8,0,0,83,85,
        3,14,7,0,84,83,1,0,0,0,84,85,1,0,0,0,85,13,1,0,0,0,86,87,5,22,0,
        0,87,91,5,7,0,0,88,90,3,8,4,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,
        1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,95,5,8,0,0,
        95,15,1,0,0,0,96,97,5,23,0,0,97,98,5,2,0,0,98,99,3,20,10,0,99,100,
        5,4,0,0,100,104,5,7,0,0,101,103,3,8,4,0,102,101,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,
        1,0,0,0,107,108,5,8,0,0,108,17,1,0,0,0,109,110,5,24,0,0,110,111,
        5,2,0,0,111,112,3,20,10,0,112,113,5,4,0,0,113,114,5,5,0,0,114,19,
        1,0,0,0,115,116,6,10,-1,0,116,117,5,2,0,0,117,118,3,20,10,0,118,
        119,5,4,0,0,119,123,1,0,0,0,120,123,5,27,0,0,121,123,5,28,0,0,122,
        115,1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,135,1,0,0,0,124,
        125,10,6,0,0,125,126,7,0,0,0,126,134,3,20,10,7,127,128,10,5,0,0,
        128,129,7,1,0,0,129,134,3,20,10,6,130,131,10,4,0,0,131,132,7,2,0,
        0,132,134,3,20,10,5,133,124,1,0,0,0,133,127,1,0,0,0,133,130,1,0,
        0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,21,1,0,0,
        0,137,135,1,0,0,0,12,25,27,45,55,64,79,84,91,104,122,133,135
    ]

class MiniParParser ( Parser ):

    grammarFileName = "MiniPar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'chan'", "'('", "','", "')'", "';'", 
                     "'seq'", "'{'", "'}'", "'par'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "'if'", "'else'", "'while'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "ELSE", "WHILE", "PRINT", "NEWLINE", 
                      "WHITESPACE", "ID", "INT", "ADDR" ]

    RULE_prog = 0
    RULE_channel = 1
    RULE_seq = 2
    RULE_par = 3
    RULE_stmt = 4
    RULE_atribuicao = 5
    RULE_condicional = 6
    RULE_condicional_else = 7
    RULE_loop = 8
    RULE_print = 9
    RULE_expr = 10

    ruleNames =  [ "prog", "channel", "seq", "par", "stmt", "atribuicao", 
                   "condicional", "condicional_else", "loop", "print", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    IF=21
    ELSE=22
    WHILE=23
    PRINT=24
    NEWLINE=25
    WHITESPACE=26
    ID=27
    INT=28
    ADDR=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def channel(self):
            return self.getTypedRuleContext(MiniParParser.ChannelContext,0)


        def EOF(self):
            return self.getToken(MiniParParser.EOF, 0)

        def seq(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.SeqContext)
            else:
                return self.getTypedRuleContext(MiniParParser.SeqContext,i)


        def par(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.ParContext)
            else:
                return self.getTypedRuleContext(MiniParParser.ParContext,i)


        def getRuleIndex(self):
            return MiniParParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MiniParParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.channel()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==9:
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 23
                    self.seq()
                    pass
                elif token in [9]:
                    self.state = 24
                    self.par()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(MiniParParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniParParser.ID, 0)

        def ADDR(self):
            return self.getToken(MiniParParser.ADDR, 0)

        def getRuleIndex(self):
            return MiniParParser.RULE_channel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChannel" ):
                listener.enterChannel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChannel" ):
                listener.exitChannel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChannel" ):
                return visitor.visitChannel(self)
            else:
                return visitor.visitChildren(self)




    def channel(self):

        localctx = MiniParParser.ChannelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_channel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MiniParParser.T__0)
            self.state = 33
            self.match(MiniParParser.T__1)
            self.state = 34
            self.match(MiniParParser.ID)
            self.state = 35
            self.match(MiniParParser.T__2)
            self.state = 36
            self.match(MiniParParser.ADDR)
            self.state = 37
            self.match(MiniParParser.T__3)
            self.state = 38
            self.match(MiniParParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniParParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniParParser.RULE_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq" ):
                return visitor.visitSeq(self)
            else:
                return visitor.visitChildren(self)




    def seq(self):

        localctx = MiniParParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_seq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MiniParParser.T__5)
            self.state = 41
            self.match(MiniParParser.T__6)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 161480704) != 0):
                self.state = 42
                self.stmt()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(MiniParParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniParParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniParParser.RULE_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)




    def par(self):

        localctx = MiniParParser.ParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_par)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MiniParParser.T__8)
            self.state = 51
            self.match(MiniParParser.T__6)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 161480704) != 0):
                self.state = 52
                self.stmt()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(MiniParParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(MiniParParser.AtribuicaoContext,0)


        def condicional(self):
            return self.getTypedRuleContext(MiniParParser.CondicionalContext,0)


        def loop(self):
            return self.getTypedRuleContext(MiniParParser.LoopContext,0)


        def print_(self):
            return self.getTypedRuleContext(MiniParParser.PrintContext,0)


        def getRuleIndex(self):
            return MiniParParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniParParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.atribuicao()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.condicional()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.loop()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.print_()
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


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniParParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniParParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniParParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = MiniParParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MiniParParser.ID)
            self.state = 67
            self.match(MiniParParser.T__9)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(MiniParParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniParParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniParParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniParParser.StmtContext,i)


        def condicional_else(self):
            return self.getTypedRuleContext(MiniParParser.Condicional_elseContext,0)


        def getRuleIndex(self):
            return MiniParParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = MiniParParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(MiniParParser.IF)
            self.state = 72
            self.match(MiniParParser.T__1)
            self.state = 73
            self.expr(0)
            self.state = 74
            self.match(MiniParParser.T__3)
            self.state = 75
            self.match(MiniParParser.T__6)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 161480704) != 0):
                self.state = 76
                self.stmt()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(MiniParParser.T__7)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 83
                self.condicional_else()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condicional_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniParParser.ELSE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniParParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniParParser.RULE_condicional_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional_else" ):
                listener.enterCondicional_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional_else" ):
                listener.exitCondicional_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional_else" ):
                return visitor.visitCondicional_else(self)
            else:
                return visitor.visitChildren(self)




    def condicional_else(self):

        localctx = MiniParParser.Condicional_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicional_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(MiniParParser.ELSE)
            self.state = 87
            self.match(MiniParParser.T__6)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 161480704) != 0):
                self.state = 88
                self.stmt()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(MiniParParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniParParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniParParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniParParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniParParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MiniParParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MiniParParser.WHILE)
            self.state = 97
            self.match(MiniParParser.T__1)
            self.state = 98
            self.expr(0)
            self.state = 99
            self.match(MiniParParser.T__3)
            self.state = 100
            self.match(MiniParParser.T__6)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 161480704) != 0):
                self.state = 101
                self.stmt()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(MiniParParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniParParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniParParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniParParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = MiniParParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MiniParParser.PRINT)
            self.state = 110
            self.match(MiniParParser.T__1)
            self.state = 111
            self.expr(0)
            self.state = 112
            self.match(MiniParParser.T__3)
            self.state = 113
            self.match(MiniParParser.T__4)
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
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniParParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniParParser.ExprContext,i)


        def ID(self):
            return self.getToken(MiniParParser.ID, 0)

        def INT(self):
            return self.getToken(MiniParParser.INT, 0)

        def getRuleIndex(self):
            return MiniParParser.RULE_expr

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
        localctx = MiniParParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 116
                self.match(MiniParParser.T__1)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(MiniParParser.T__3)
                pass
            elif token in [27]:
                self.state = 120
                self.match(MiniParParser.ID)
                pass
            elif token in [28]:
                self.state = 121
                self.match(MiniParParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 133
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MiniParParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 124
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 125
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniParParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 127
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 128
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 129
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = MiniParParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 131
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 132
                        self.expr(5)
                        pass

             
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




