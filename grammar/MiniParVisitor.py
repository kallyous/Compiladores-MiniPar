# Generated from MiniPar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniParParser import MiniParParser
else:
    from MiniParParser import MiniParParser

# This class defines a complete generic visitor for a parse tree produced by MiniParParser.

class MiniParVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniParParser#prog.
    def visitProg(self, ctx:MiniParParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#channel.
    def visitChannel(self, ctx:MiniParParser.ChannelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#seq.
    def visitSeq(self, ctx:MiniParParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#par.
    def visitPar(self, ctx:MiniParParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#stmt.
    def visitStmt(self, ctx:MiniParParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#atribuicao.
    def visitAtribuicao(self, ctx:MiniParParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#condicional.
    def visitCondicional(self, ctx:MiniParParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#condicional_else.
    def visitCondicional_else(self, ctx:MiniParParser.Condicional_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#loop.
    def visitLoop(self, ctx:MiniParParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#print.
    def visitPrint(self, ctx:MiniParParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniParParser#expr.
    def visitExpr(self, ctx:MiniParParser.ExprContext):
        return self.visitChildren(ctx)



del MiniParParser