from enum import Enum

lines_re = "(.|\n)"


class BaseBlockRegex(Enum):
    COMMAND = f'({lines_re}*)'
    DEF_MACRO = f'#({lines_re}*)'
    OBJECT_NAME = f'`{lines_re}+`'


class DefmacroRegex(Enum):
    NAME = f'({lines_re}+)'
    ARG = f'`{lines_re}+`'
    PY_BLOCK = f'py ({lines_re}*)'


class KeywordBlock:

    def __init__(self, regex, py_code):
        self.re = regex
        self.py = py_code
