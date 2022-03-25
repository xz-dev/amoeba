from .object_type import ObjectType
from .link_grammar import LinkGrammar


class Object:

    def __init__(self, name: str, obj_type: ObjectType, value,
                 grammar_link: LinkGrammar):
        self.name = name
        self.type = obj_type
        self.value = value
        self.grammar_link = LinkGrammar
