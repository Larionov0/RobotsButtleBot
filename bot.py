import requests
from time import sleep
from random import choice


class Bot:
    url = "https://api.telegram.org"
    last_update_id = 0

    def __init__(self, token):
        self.token = token
        self.set_last_update_id_from_file()

    def run(self):
        while True:
            new_updates = self.get_new_updates()
            for update in new_updates:
                self.give_answer(update)
            sleep(2)

    def give_answer(self, update):
        chat_id = self.get_chat_id_from_update(update)
        text = self.get_message_text_from_update(update)
        hello = False

        if any([word in text.lower() for word in ["привет", "привки", "хай", "hi", "hello", "what`s up"]]):
            hello = True

        if hello:
            answer_text = choice(["Привет, друг", "Приветики", "Hello bro"])
        else:
            answer_text = "Пока не умею отвечать на это предложение!"

        self.send_message(chat_id, answer_text)


    @staticmethod
    def get_message_text_from_update(update):
        return update["message"]["text"]

    def get_updates(self):
        r = requests.get(f"{self.url}/bot{self.token}/getUpdates")
        dct = r.json()
        updates = dct['result']
        return updates

    def send_message(self, chat_id, text):
        requests.get(f"{self.url}/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}")

    def get_new_updates(self):
        updates = self.get_updates()
        new_updates = []
        i = len(updates) - 1
        while i >= 0:
            update = updates[i]
            id = update["update_id"]
            if id <= self.last_update_id:  # значит, сообщение старое
                break
            new_updates.insert(0, update)
            i -= 1

        if len(new_updates) != 0:
            last_update = new_updates[-1]
            id = last_update['update_id']
            self.set_last_update_id(id)

        return new_updates

    def set_last_update_id(self, id):
        self.last_update_id = id
        self.save_last_update_id()

    def save_last_update_id(self):
        with open("data/last_update_id.txt", 'wt') as file:
            file.write(str(self.last_update_id))

    def set_last_update_id_from_file(self):
        try:
            with open("data/last_update_id.txt", 'rt') as file:
                self.last_update_id = int(file.read())
        except:
            self.last_update_id = 0

    @staticmethod
    def get_chat_id_from_update(update):
        return update['message']['chat']['id']
