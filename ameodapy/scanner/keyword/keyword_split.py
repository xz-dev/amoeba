from .keyword_match import KeywordMatch
from .keyword_tree import KeywordTreeNode


def get_keyword_search_tree(keyword_list: tuple[list[str]]):
    return [
        init_keyword_search_tree(keyword_list) for keword_list in keyword_list
    ]


def init_keyword_search_tree(keyword_list: list[str]) -> KeywordTreeNode:
    root_node = KeywordTreeNode('', None)
    for keyword in keyword_list:
        keyword = keyword.name
        node = root_node
        for char in keyword:
            next_node = node.get_node(char)
            if next_node is None:
                next_node = KeywordTreeNode(char, node)
                node.add_node(char, next_node)
            node = next_node
        node.have_word()
    return root_node


def split_keyword(command_str: str,
                  keyword_list: tuple[list[str]]) -> list[str]:
    """Participle,
    split string to a keyword list
    """
    keyword_tree_list = get_keyword_search_tree(keyword_list)
    match = KeywordMatch(keyword_tree_list)
    keyword_list = []
    for word in match:
        match.search_word(word)
        keyword = match.get_keyword()
        if keyword:
            keyword_list += keyword
            match.reset_status()
    return keyword_list
