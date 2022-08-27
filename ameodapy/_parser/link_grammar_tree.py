from .object import Object


class LinkGrammarTreeNode:

    def __init__(self):
        self.object_map = {}
        self.var_node = None
        self.func_node = None

    def add_object(self, obj: Object):
        name = obj.name
        obj_map = self.object_map
        if name not in obj_map:
            obj_map[name] = {obj}
        else:
            obj_map[name].add(obj)
