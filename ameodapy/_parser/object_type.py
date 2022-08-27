from enum import Enum
from .link_grammar import LinkGrammar


class ObjectTypeEnum(Enum):
    VARIABLE = "VARIABLE"
    NAME = "NAME"
    MARKER = "MARKER"


class ObjectType:

    def __init__(self, type: ObjectTypeEnum):
        self.type = type
        self.grammar_link = None

    def grammar_link(self, grammar_link: LinkGrammar):
        self.grammar_link = grammar_link
