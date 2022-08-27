from .object import BaseObject


class Value(BaseObject):

    def __init__(self, name, value):
        super().__init__(name, value)
        self.value = self.obj
