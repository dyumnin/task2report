from antlr4 import *
from .grammar.task2reportLexer import task2reportLexer
from .grammar.task2reportListener import task2reportListener
from .grammar.task2reportParser import task2reportParser
import sys
import os

class task2reportPrintListener(task2reportListener):
    def __init__(self,outfile):
        self.of=open(outfile,'w')
        super().__init__()

    def enterBullet(self, ctx):
        print(f"# {ctx.string().getText()}",file=self.of)
    def enterHex(self,ctx):
        path=os.path.expanduser(f"~/tasknotes/{ctx.getText()}.md")
        if os.path.exists(path):
            with open(path,'r') as r:
                print(r.read(),file=self.of)
    

def runParser(infile,outfile):
    lexer = task2reportLexer(FileStream(infile))
    stream = CommonTokenStream(lexer)
    parser = task2reportParser(stream)
    tree = parser.top()
    printer = task2reportPrintListener(outfile)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    runParser()
