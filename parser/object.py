from .object_type import ObjectType


class Object:

    def __init__(self):
        self.name = None
        self.obj_type = None
        self.value = None

    def name(self, name: str):
        self.name = name
        return self

    def obj_type(self, obj_type: ObjectType):
        self.obj_type = obj_type
        return self

    def value(self, value):
        self.value = value
        return self
