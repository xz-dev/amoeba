class KeywordTreeNode:
    """Keyword Trie
    """

    def __init__(self, word, parent_node):
        self.char = word
        self.parent_node = parent_node
        self.node_map = {}
        self.have_word: bool = False

    def add_node(self, char: str, node):
        try:
            self.node_map[char].add(node)
        except KeyError:
            self.node_map[char] = {node}

    def get_node(self, word: str):
        try:
            return self.node_map[word]
        except KeyError:
            pass

    def have_word(self):
        self.have_word = True

    def get_keyword(self) -> str:
        node = self
        keyword = ''
        while node:
            keyword += node.char
            node = node.parent_node
