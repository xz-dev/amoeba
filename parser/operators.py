from .object_type import ObjectType, ObjectTypeEnum
from .link_grammar import LinkGrammar, LinkGrammarSideNode


class Oprator:

    def __init__(self):
        self.obj = Object()

    def name(self, name):
        self.name = name


def make_oprator():
    print_love = Object(
        "love",
        ObjectType(ObjectTypeEnum.NAME, LinkGrammar(LinkGrammarSideNode())))
