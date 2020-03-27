from GameObjects import *


class State:
    type: str
    all_types = ['прохлаждается', 'в бою']

    def __init__(self, type_):
        self.type = type_


class User:
    chat_id: int
    state: State
    hero: Hero

    players = []

    def __init__(self, chat_id, message_id):
        self.chat_id = chat_id
        self.message_id = message_id
        self.state = State('прохлаждается')
        self.hero = None
        self.players.append(self)


class Users:
    def __init__(self):
        self.list = []

    def __getitem__(self, i):
        return self.list[i]

    def append(self, user):
        self.list.append(user)

    def find_user_by_chat_id(self, chat_id):
        for user in self.list:
            if user.chat_id == chat_id:
                return user
        return False
