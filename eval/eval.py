from grammar.grammar import *

# 評価関数
def eval_echoln(tokens):
    code = tokens[1]  # 引用符を除去
    print(code)

# パースアクション
expr.setParseAction(eval_echoln)