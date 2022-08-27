from enum import Enum
from .base.base_syntax_regex import BaseBlockRegex


class SyntaxStatusMap(Enum):
    COMMAND = 1
    DEF_MACRO = 2
    FUNTION = 3


syntax_regex_map = {
    BaseBlockRegex.COMMAND: SyntaxStatusMap.COMMAND,
    BaseBlockRegex.DEF_MACRO: SyntaxStatusMap.DEF_MACRO,
}


def add_synctax_regex(synctax_regex):
    syntax_regex_map[synctax_regex] = SyntaxStatusMap.FUNTION
