from json import dumps
from bot import Bot
from misc import token

url = 'https://api.telegram.org'


def print_structure(struct):
    print(dumps(struct, indent=4))


def main():
    bot = Bot(token)

    update = bot.get_updates()[-1]
    chat_id = bot.get_chat_id_from_update(update)
    bot.send_message(chat_id, "I am too")


if __name__ == "__main__":
    main()
