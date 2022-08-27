from enum import Enum

from .keyword_search_tree import KeywordTreeNode


class MatchTreeStatus(Enum):
    MATCH = 1
    END = 0
    FAIL = -1


class KeywordMatch:
    """Match keyword via Trie,
    match high priority first.
    """

    def __init__(self, keyword_tree_list: list[KeywordTreeNode]):
        self.keyword_node = None
        self.keyword_tree_list = keyword_tree_list
        self.keyword_tree_root_list = keyword_tree_list

    def search_word(self, char):
        trash_node_list = []
        for index in len(self.keyword_tree_root_list):
            node = self.keyword_tree_root_list[index]
            status, next_node = self.search_tree(node, char)
            if status == MatchTreeStatus.MATCH:
                self.keyword_tree_root_list[index] = next_node
            elif status == MatchTreeStatus.END:
                self.keyword_node = node
            elif status == MatchTreeStatus.FAIL:
                trash_node_list.append(node)
        self.keyword_tree_root_list = [
            node for node in self.keyword_tree_root_list
            if node not in trash_node_list
        ]

    @staticmethod
    def search_tree(node: KeywordTreeNode,
                    char) -> tuple[MatchTreeStatus, KeywordTreeNode]:
        next_node = node.get_node()
        if next_node:
            return MatchTreeStatus.MATCH, next_node
        elif next_node.end_word_set:
            return MatchTreeStatus.END, next_node
        else:
            return MatchTreeStatus.FAIL, None

    def record_word(self, char):
        if char not in (' ', '\n') or self.keyword_record:
            self.keyword_record += char

    def reset_status(self):
        self.keyword_node = None
        self.keyword_tree_root_list = self.keyword_tree_list[:]

    def get_keyword(self) -> str or None:
        if self.keyword_node:
            return self.keyword_node.get_keyword()
        else:
            return None
