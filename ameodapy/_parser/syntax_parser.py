from .context import Context
from .syntax_tree import SyntaxTreeNode

# 最少未知数、最少变量语法分析


class SyntaxParser:

    def __init__(self, keyword_list: str, context: Context):
        self.context = context

    def hungry_match(self):
        root_node = SyntaxTreeNode(None, "+")
