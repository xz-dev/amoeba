import re

from .block_regex import BaseBlockRegex


def split_block(s: str):
    command_s_match = re.match(BaseBlockRegex.COMMAND, s)
    command_s_list = command_s_match.groups()
    return command_s_list
