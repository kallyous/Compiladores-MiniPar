import sys
import io
from antlr4 import *
from grammar.MiniParLexer import MiniParLexer
from grammar.MiniParParser import MiniParParser
from MiniParSemantic import MiniParSemantic
from MiniParInterpreter import MiniParInterpreter
# from VisitorInterp import VisitorInterp

def main(argv):

    try:
        input_stream = FileStream(argv[1])
    except (FileNotFoundError, OSError, IndexError):
        input_stream = StdinStream()

    lexer = MiniParLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniParParser(stream)
    tree = parser.prog()  # Constrói árvore sintática com prog sendo a raiz.
    semantic = MiniParSemantic()
    walker = ParseTreeWalker()
    walker.walk(semantic, tree)  # Navega árvore em profundidade pela esquerda, fazendo análise lexico-sintática.
    interpreter = MiniParInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main(sys.argv)