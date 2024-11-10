from grammar.MiniParListener import MiniParListener

class MiniParSemantic (MiniParListener):
    variables = []
    channel = False

    def exitChannel(self, ctx):
        self.channel = True

    def exitProg(self, ctx):
        if not self.channel:
            raise Exception("Canal não declarado")

    def exitAtribuicao(self, ctx):
        var = ctx.ID().getText()
        self.variables.append(var)

    def exitExpr(self, ctx):
        if ctx.ID() and not ctx.ID().getText() in self.variables:
            raise Exception("Variável não declarada: " + ctx.ID().getText())
