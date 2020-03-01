import requests


class Bot:
    url = "https://api.telegram.org"

    def __init__(self, token):
        self.token = token

    def get_updates(self):
        r = requests.get(f"{self.url}/bot{self.token}/getUpdates")
        dct = r.json()
        updates = dct['result']
        return updates

    def send_message(self, chat_id, text):
        requests.get(f"{self.url}/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}")

    @staticmethod
    def get_chat_id_from_update(update):
        return update['message']['chat']['id']
