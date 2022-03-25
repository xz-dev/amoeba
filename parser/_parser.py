from .syntax.syntax_tree import SyntaxTreeNode
from enum import Enum


class CodeBlockType(Enum):
    COMMAND = 0
    OBJECT_NAME = 1
    DEF_MACRO = 2


class CodeBlock:

    def __init__(self, block_type: CodeBlockType, code_str: str):
        self.type = None


def split_code(code_str) -> list[str]:
    name_list = []
    status = None
    name = ""
    while code_str:
        c, code_str = code_str[:1], code_str[1:]
        if c == '`':
            if status == CodeBlockType.OBJECT_NAME:
                status = None
                name_list.append(name)
            else:
                status = CodeBlockType.OBJECT_NAME
        elif status == CodeBlockType.OBJECT_NAME:
            name += c
        elif c and not c.isspace():
            name += c
        else:
            name_list.append(name)
    return name_list
