from .base_operator import BaseOperator


class DefmacroOperator(BaseOperator):

    def __init__(self):
        super().__init__(self, 'defmacro', self.register)

    @staticmethod
    def register(macro_name, *args):
        pass
