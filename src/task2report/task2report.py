from antlr4 import *
from .grammar.task2reportLexer import Lexer
from .grammar.task2reportListener import Listener
from .grammar.task2reportParser import Parser
import sys
import os

class PrintListener(Listener):
    def enterBullet(self, ctx):
        print(f"# {ctx.string().getText()}")
    def enterHex(self,ctx):
        path=os.path.expanduser(f"~/tasknotes/{ctx.getText()}.md")
        if os.path.exists(path):
            with open(path,'r') as r:
                print(r.read())
    

def runParser(file):
    lexer = Lexer(FileStream(file))
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.top()
    printer = PrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    runParser()
