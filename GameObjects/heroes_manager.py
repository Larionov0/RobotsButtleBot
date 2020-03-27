from GameObjects.creatures import *


def menu():
    filename = 'heroes.json'
    try:
        with open(filename) as file:
            heroes = load(file)
        if type(heroes) is not list:
            heroes = []
    except:
        heroes = []

    while True:
        print('1 - добавить персонажа')
        print('2 - удалить персонажа')
        print('3 - выйти')

        choice = input()
        if choice == "1":
            hero = HeroPrototype.create_from_user()
            hero_dict = hero.to_dict()
            heroes.append(hero_dict)
            json = dumps(heroes, indent=4)
            with open(filename, 'wt') as file:
                file.write(json)

        elif choice == '3':
            break


def main():
    menu()


if __name__ == '__main__':
    main()
