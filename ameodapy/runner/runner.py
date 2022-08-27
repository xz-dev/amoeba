from ameodapy.scanner.block.block_split import split_block
from ameodapy.scanner.keyword.keyword_split import split_keyword

keyword_tuple = (['print'])


def run(s: str):
    command_s_list = split_block(s)
    for command_s in command_s_list:
        keyword_s_list = split_keyword(command_s, keyword_tuple)
