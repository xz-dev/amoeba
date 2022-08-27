from .object import BaseObject


class BaseOperator(BaseObject):

    def __init__(self, name, function):
        super().__init__(name, function)
        self.function = self.obj
