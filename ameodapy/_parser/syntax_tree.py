from .object import Object


class SyntaxTreeNode:

    def __init__(self, root, operator: Object):
        self.root = root
        self.operator = operator
        self.objects = []
