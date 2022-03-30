from .object import Object
from .keyword_search_tree import KeywordSearchTreeNode
from .keyword_match import KeywordMatch
from .context import Context


def get_keyword_search_tree(object_list_pair: tuple[list[Object]]):
    hp_object_list, object_list = object_list_pair
    return (init_keyword_search_tree(hp_object_list),
            init_keyword_search_tree(object_list))


def init_keyword_search_tree(
        object_list: list[Object]) -> KeywordSearchTreeNode:
    root_node = KeywordSearchTreeNode('', None)
    for obj in object_list:
        keyword = obj.name
        node = root_node
        for word in keyword:
            next_node = node.get_node(word)
            if next_node is None:
                next_node = KeywordSearchTreeNode(word, node)
                node.add_node(word, next_node)
            node = next_node
        node.add_end_keyword_object(obj)
    return root_node


def parser_keyword_list(command_str: str, context: Context) -> list[str]:
    object_list_map = context.get_object_list_pair()
    hp_object_node, object_node = get_keyword_search_tree(object_list_map)
    match = KeywordMatch(hp_object_node, object_node)
    keyword_list = []
    for word in match:
        match.search_word(word)
        keyword = match.get_keyword()
        if keyword:
            keyword_list += keyword
            match.reset_status()
    return keyword_list
