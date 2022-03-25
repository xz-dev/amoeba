class State:

    def __init__(self, *atom):
        self.atom_list = atom


class Atom:

    def __init__(self, name, value):
        self.name = name
        self.value = value
