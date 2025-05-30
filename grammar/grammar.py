from pyparsing import *

# キーワード定義
ECHOLN = Keyword("echoln")

STRING = QuotedString('"')

SEMI   = Suppress(";")

# 文法定義
expr = (ECHOLN + STRING + SEMI)

# プログラム定義
program = OneOrMore(expr) + StringEnd()