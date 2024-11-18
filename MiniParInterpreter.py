from grammar.MiniParVisitor import MiniParVisitor
import socket
import threading

class MiniParInterpreter (MiniParVisitor):
    variables = {}
    channel = None

    def visitChannel(self, ctx):
        self.channel = ctx.ADDR().getText()

    def visitPar(self, ctx):
        async_thread = threading.Thread(target=self.visitChildren, args=(ctx,))
        async_thread.start()

    def visitAtribuicao(self, ctx):
        var = ctx.ID().getText()
        val = self.visit(ctx.expr())
        self.variables[var] = val

    def visitCondicional(self, ctx):
        if self.visit(ctx.expr()):
            for t in ctx.stmt():
                self.visit(t)
        elif ctx.condicional_else() is not None:
            for t in ctx.condicional_else.stmt():
                self.visit(t)

    def visitLoop(self, ctx):
        while self.visit(ctx.expr()):
            for t in ctx.stmt():
                self.visit(t)

    def visitPrint(self, ctx):
        print(self.visit(ctx.expr()))

    def visitExpr(self, ctx):
        if ctx.ID():
            return self.variables[ctx.ID().getText()]
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        if ctx.op is not None:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            eval_str = str(left) + ctx.op.text + str(right)
        else:
            eval_str = self.visit(ctx.expr(0))

        host, port = self.channel.split(':')
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # print('Connecting to', host, int(port), 'to send', eval_str)
                s.connect((host, int(port)))
                s.sendall(eval_str.encode())
                data = s.recv(1024).decode()
                if data == 'None':
                    return None
                if data == 'True':
                    return True
                if data == 'False':
                    return False
                if data.startswith('Error'):
                    raise Exception(data)
                return data

        except ConnectionRefusedError as e:
            print(f"ERRO: Servidor não encontrado em {host}:{port}")
            print(e)
            exit(1)