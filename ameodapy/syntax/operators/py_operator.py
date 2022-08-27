from ..objects.base_object import BaseObject
from .base_operator import BaseOperator


class PyWapperOperator(BaseOperator):

    def __init__(self, name, py_code):
        function = self.run_py
        super().__init__(self, name, function)

    def run_py(self, *objects):
        return self.run_py_wapper(self.py_code, *objects)

    @staticmethod
    def run_py_wapper(py_code, objects: list[BaseObject]):
        locals_dict = {}
        global_dict = {obj.name: obj.value for obj in objects}
        exec(py_code, global_dict, locals_dict)
        for obj in objects:
            obj.value = locals_dict[obj.name]

    def __str__(self):
        return f"py_operator `{self.name}`"
