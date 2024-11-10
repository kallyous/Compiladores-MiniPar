import sys
from antlr4 import *
from grammar.MiniParLexer import MiniParLexer
from grammar.MiniParParser import MiniParParser
from MiniParSemantic import MiniParSemantic
from MiniParInterpreter import MiniParInterpreter
# from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniParLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniParParser(stream)
    tree = parser.prog()
    semantic = MiniParSemantic()
    walker = ParseTreeWalker()
    walker.walk(semantic, tree)
    interpreter = MiniParInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main(sys.argv)