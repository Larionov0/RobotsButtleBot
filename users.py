class User:
    def __init__(self, chat_id, message_id):
        self.chat_id = chat_id
        self.message_id = message_id


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

