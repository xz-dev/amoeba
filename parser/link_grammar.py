from .object_type import ObjectType
from .object import Object


class LinkGrammar:

    def __init__(self, left_dep_list: list[ObjectType.VARIABLE or Object],
                 right_dep_list: list[ObjectType.VARIABLE or Object]):
        self.left_dep_list = left_dep_list
        self.right_dep_list = right_dep_list
