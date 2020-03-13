import requests
from time import sleep
from random import choice
from tools import *


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

    def answer_callback_query(self, callback_query_id):
        requests.get(f"{self.url}/bot{self.token}/answerCallbackQuery?callback_query_id={callback_query_id}")

    def give_answer_to_text_message(self, update):
        chat_id = self.get_chat_id_from_update(update)
        text = self.get_message_text_from_update(update)

        if text == "/start":
            b1 = Button('играть', callback_data='game')
            b2 = Button('магазин', callback_data='store')
            b3 = Button('Ознакомиться с правилами', callback_data="rules")
            r1 = Row([b1])
            r2 = Row([b2])
            r3 = Row([b3])
            k = Keyboard([r1, r2, r3])

            self.send_message(chat_id, "Выберите пункт:", keyboard=k)

        else:
            if any([word in text.lower() for word in ["привет", "привки", "хай", "hi", "hello", "what`s up"]]):
                answer_text = choice(["Привет, друг", "Приветики", "Hello bro"])
            else:
                answer_text = "Пока не умею отвечать на это предложение!"

            self.send_message(chat_id, answer_text)

    def give_answer_to_button_pressing(self, update):
        callback_query_id = update["callback_query"]["id"]
        chat_id = update['callback_query']['message']['chat']['id']
        callback_data = update['callback_query']['data']

        if callback_data == "rules":
            self.send_message(chat_id, "Правила таковы: ты ры пы ры тра ли ва ли🤩")
        elif callback_data == "store":
            b1 = Button('пупсень', "Pupsen")
            b2 = Button('вупсень', "Vupsen")
            r1 = Row([b1])
            r2 = Row([b2])
            k = Keyboard([r1, r2])
            self.send_message(chat_id, "Магазин: ", keyboard=k)
        elif callback_data == "Pupsen":
            self.send_message(chat_id, "Пупсень пока недоступен!")

        self.answer_callback_query(callback_query_id)

    def give_answer(self, update):
        if "callback_query" in update:
            self.give_answer_to_button_pressing(update)
        else:
            self.give_answer_to_text_message(update)

    @staticmethod
    def get_message_text_from_update(update):
        return update["message"]["text"]

    def get_updates(self):
        r = requests.get(f"{self.url}/bot{self.token}/getUpdates")
        dct = r.json()
        updates = dct['result']
        return updates

    def send_message(self, chat_id, text, keyboard=None):
        if keyboard:
            requests.get(f"{self.url}/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}&reply_markup=" + '{"inline_keyboard": ' + keyboard.to_json() + '}')
        else:
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
