from .context import Context
from .syntax_tree import SyntaxTreeNode

# 最少未知数、最少变量语法分析

base_context = Context(None)
base_context.add_object()


def parser_syntax_tree(command_str: str, context: Context) -> SyntaxTreeNode:
    pass
