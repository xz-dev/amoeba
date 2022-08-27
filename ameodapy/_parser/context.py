from .object_type import ObjectType
from .object import Object


class Context:

    def __init__(self, parent_context):
        self.parent = parent_context
        self.objects: dict[ObjectType, list[Object]] = {}

    def add_object(self, obj: Object):
        object_type = obj.type
        try:
            self.objects[object_type].append(obj)
        except KeyError:
            self.objects[object_type] = [obj]

    def get_all_object(self) -> dict[ObjectType, list[Object]]:
        objects = {}
        context = self
        while context:
            for key, object_list in context.objects.items():
                try:
                    objects[key] += object_list
                except KeyError:
                    objects[key] = object_list
                context = context.parent
        return objects

    def get_object_list_pair(self):
        hp_object_list = []
        object_list = []
        for obj_type, obj_list in self.get_all_object().items():
            if obj_type in {
                    ObjectType.FUNCTION, ObjectType.MULTI_KEYWORD_FUNCTION
            }:
                hp_object_list += obj_list
            else:
                object_list += obj_list
        return hp_object_list, object_list
