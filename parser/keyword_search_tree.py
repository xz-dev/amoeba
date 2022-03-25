from .object import Object


class KeywordSearchTreeNode:

    def __init__(self, word, parent_node):
        self.word = word
        self.parent_node = parent_node
        self.node_map = {}
        self.end_keyword_object_set: set[Object] = set()

    def add_node(self, word: str, node):
        try:
            self.node_map[word].add(node)
        except KeyError:
            self.node_map[word] = {node}

    def get_node(self, word: str):
        try:
            return self.node_map[word]
        except KeyError:
            pass

    def add_end_keyword_object(self, obj):
        self.end_keyword_object_set.add(obj)

    def get_keyword(self) -> str:
        node = self
        keyword = ''
        while node:
            keyword += node.word
            node = node.parent_node
