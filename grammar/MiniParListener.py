# Generated from MiniPar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniParParser import MiniParParser
else:
    from MiniParParser import MiniParParser

# This class defines a complete listener for a parse tree produced by MiniParParser.
class MiniParListener(ParseTreeListener):

    # Enter a parse tree produced by MiniParParser#prog.
    def enterProg(self, ctx:MiniParParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniParParser#prog.
    def exitProg(self, ctx:MiniParParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniParParser#channel.
    def enterChannel(self, ctx:MiniParParser.ChannelContext):
        pass

    # Exit a parse tree produced by MiniParParser#channel.
    def exitChannel(self, ctx:MiniParParser.ChannelContext):
        pass


    # Enter a parse tree produced by MiniParParser#seq.
    def enterSeq(self, ctx:MiniParParser.SeqContext):
        pass

    # Exit a parse tree produced by MiniParParser#seq.
    def exitSeq(self, ctx:MiniParParser.SeqContext):
        pass


    # Enter a parse tree produced by MiniParParser#par.
    def enterPar(self, ctx:MiniParParser.ParContext):
        pass

    # Exit a parse tree produced by MiniParParser#par.
    def exitPar(self, ctx:MiniParParser.ParContext):
        pass


    # Enter a parse tree produced by MiniParParser#stmt.
    def enterStmt(self, ctx:MiniParParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniParParser#stmt.
    def exitStmt(self, ctx:MiniParParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniParParser#atribuicao.
    def enterAtribuicao(self, ctx:MiniParParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by MiniParParser#atribuicao.
    def exitAtribuicao(self, ctx:MiniParParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by MiniParParser#condicional.
    def enterCondicional(self, ctx:MiniParParser.CondicionalContext):
        pass

    # Exit a parse tree produced by MiniParParser#condicional.
    def exitCondicional(self, ctx:MiniParParser.CondicionalContext):
        pass


    # Enter a parse tree produced by MiniParParser#condicional_else.
    def enterCondicional_else(self, ctx:MiniParParser.Condicional_elseContext):
        pass

    # Exit a parse tree produced by MiniParParser#condicional_else.
    def exitCondicional_else(self, ctx:MiniParParser.Condicional_elseContext):
        pass


    # Enter a parse tree produced by MiniParParser#loop.
    def enterLoop(self, ctx:MiniParParser.LoopContext):
        pass

    # Exit a parse tree produced by MiniParParser#loop.
    def exitLoop(self, ctx:MiniParParser.LoopContext):
        pass


    # Enter a parse tree produced by MiniParParser#print.
    def enterPrint(self, ctx:MiniParParser.PrintContext):
        pass

    # Exit a parse tree produced by MiniParParser#print.
    def exitPrint(self, ctx:MiniParParser.PrintContext):
        pass


    # Enter a parse tree produced by MiniParParser#expr.
    def enterExpr(self, ctx:MiniParParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniParParser#expr.
    def exitExpr(self, ctx:MiniParParser.ExprContext):
        pass



del MiniParParser