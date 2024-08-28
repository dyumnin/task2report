# Generated from grammar/task2report.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .task2reportParser import task2reportParser
else:
    from task2reportParser import task2reportParser

# This class defines a complete listener for a parse tree produced by task2reportParser.
class task2reportListener(ParseTreeListener):

    # Enter a parse tree produced by task2reportParser#top.
    def enterTop(self, ctx:task2reportParser.TopContext):
        pass

    # Exit a parse tree produced by task2reportParser#top.
    def exitTop(self, ctx:task2reportParser.TopContext):
        pass


    # Enter a parse tree produced by task2reportParser#heading.
    def enterHeading(self, ctx:task2reportParser.HeadingContext):
        pass

    # Exit a parse tree produced by task2reportParser#heading.
    def exitHeading(self, ctx:task2reportParser.HeadingContext):
        pass


    # Enter a parse tree produced by task2reportParser#string.
    def enterString(self, ctx:task2reportParser.StringContext):
        pass

    # Exit a parse tree produced by task2reportParser#string.
    def exitString(self, ctx:task2reportParser.StringContext):
        pass


    # Enter a parse tree produced by task2reportParser#indent.
    def enterIndent(self, ctx:task2reportParser.IndentContext):
        pass

    # Exit a parse tree produced by task2reportParser#indent.
    def exitIndent(self, ctx:task2reportParser.IndentContext):
        pass


    # Enter a parse tree produced by task2reportParser#date.
    def enterDate(self, ctx:task2reportParser.DateContext):
        pass

    # Exit a parse tree produced by task2reportParser#date.
    def exitDate(self, ctx:task2reportParser.DateContext):
        pass


    # Enter a parse tree produced by task2reportParser#star.
    def enterStar(self, ctx:task2reportParser.StarContext):
        pass

    # Exit a parse tree produced by task2reportParser#star.
    def exitStar(self, ctx:task2reportParser.StarContext):
        pass


    # Enter a parse tree produced by task2reportParser#bullet.
    def enterBullet(self, ctx:task2reportParser.BulletContext):
        pass

    # Exit a parse tree produced by task2reportParser#bullet.
    def exitBullet(self, ctx:task2reportParser.BulletContext):
        pass


    # Enter a parse tree produced by task2reportParser#hex.
    def enterHex(self, ctx:task2reportParser.HexContext):
        pass

    # Exit a parse tree produced by task2reportParser#hex.
    def exitHex(self, ctx:task2reportParser.HexContext):
        pass


    # Enter a parse tree produced by task2reportParser#tag.
    def enterTag(self, ctx:task2reportParser.TagContext):
        pass

    # Exit a parse tree produced by task2reportParser#tag.
    def exitTag(self, ctx:task2reportParser.TagContext):
        pass



del task2reportParser