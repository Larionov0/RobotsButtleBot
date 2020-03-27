from Tools.main import *


class State:
    names = ['подброшен', "упал", "грустит", "присел", "наклонен", "смеется"]
    name: str

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'class': 'state',
            'name': self.name
        }

    @classmethod
    def create_from_user(cls):
        name = input_variant(cls.names, 'Выберите состояние')
        return cls(name)
