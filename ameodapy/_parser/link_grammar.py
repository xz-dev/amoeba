from .object_type import ObjectType


class LinkGrammarSideNode:

    def __init__(self, type: ObjectType, size):
        self.size_list = *size
        self.type = type


class LinkGrammar:

    def __init__(self):
        self.left_dep_list = []
        self.right_dep_list = []

    def left(self, node: LinkGrammarSideNode):
        self.left_dep_list.append(node)

    def right(self, node: LinkGrammarSideNode):
        self.right_dep_list.append(node)
