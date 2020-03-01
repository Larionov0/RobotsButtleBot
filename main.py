from json import dumps
from bot import Bot
from misc import token


def print_structure(struct):
    print(dumps(struct, indent=4))


def main():
    bot = Bot(token)

    bot.run()


if __name__ == "__main__":
    main()
