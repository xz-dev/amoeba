from .keyword_search_tree import KeywordSearchTreeNode


class KeywordMatch:

    def __init__(self, high_priority_object_node: KeywordSearchTreeNode,
                 object_node: KeywordSearchTreeNode):
        self.keyword_record = ""
        self.hp_object_node = high_priority_object_node
        self.hp_object_node_root = high_priority_object_node
        self.object_node_root = object_node
        self.object_node = object_node
        self.final_keyword_match = False

    def search_word(self, word):
        object_node = self.object_node
        hp_object_node = self.hp_object_node
        hp_next_node = hp_object_node.get_node(word)
        if hp_next_node:
            hp_object_node = hp_next_node
        next_object_node = None
        if object_node:
            next_object_node = object_node.get_node(word)

        if not hp_next_node and hp_object_node:
            if not next_object_node:
                self.final_keyword_match = True
            else:
                hp_object_node = self.hp_object_node_root

        self.keyword_record += word
        object_node = next_object_node  # focus enable object_node change

    def reset_status(self):
        self.keyword_record = self.keyword_record[-1:]
        self.object_node = self.object_node_root
        self.hp_object_node = self.hp_object_node_root
        self.final_keyword_match = False

    def get_keyword(self) -> str or None:
        if self.final_keyword_match:
            return self.keyword_record[:-1]
        else:
            return None
