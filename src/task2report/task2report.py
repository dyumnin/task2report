from antlr4 import *
<<<<<<< before updating
from .grammar.task2reportLexer import Lexer
from .grammar.task2reportListener import Listener
from .grammar.task2reportParser import Parser
=======
from task2reportLexer import task2reportLexer
from task2reportListener import task2reportListener
from task2reportParser import task2reportParser
>>>>>>> after updating
import sys
import os

class task2reportPrintListener(task2reportListener):
    def enterBullet(self, ctx):
        print(f"# {ctx.string().getText()}")
    def enterHex(self,ctx):
        path=os.path.expanduser(f"~/tasknotes/{ctx.getText()}.md")
        if os.path.exists(path):
            with open(path,'r') as r:
                print(r.read())
    

def runParser(file):
    lexer = task2reportLexer(FileStream(file))
    stream = CommonTokenStream(lexer)
    parser = task2reportParser(stream)
    tree = parser.top()
    printer = task2reportPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    runParser()
