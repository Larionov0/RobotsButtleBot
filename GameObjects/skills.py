from Tools.main import *
from .states import State


class Skill:
    def __init__(self, name, energy, chastota, positive, negative, needs):
        self.name = name
        self.energy = energy
        self.chastota = chastota
        self.positive = positive
        self.negative = negative
        self.needs = needs


    @classmethod
    def create_skills(cls):
        skills = []
        while True:
            print("1 - создать умение")
            print("2 - закончить с умениями")

            choice = input()
            if choice == "1":
                skill = cls.create_from_user()
                skills.append(skill)
            elif choice == "2":
                break
        return skills

    @classmethod
    def create_from_user(cls):
        positive = []
        negative = []
        needs = []

        name = input("Название умения: ")

        while True:
            print("Теперь подумения:")
            print("1 - добавить позитивное подумение")
            print("2 - негативное подумение")
            print("3 - добавить необходимость")
            print("4 - перейти к оценке умения")

            choice = input()
            if choice == '1':
                sub_skill = PositiveSubSkill.create_from_user()
                if sub_skill is not None:
                    positive.append(sub_skill)

            elif choice == "2":
                sub_skill = NegativeSubSkill.create_from_user()
                if sub_skill is not None:
                    negative.append(sub_skill)

            elif choice == "3":
                need = Need.create_from_user()
                needs.append(need)

            elif choice == '4':
                break

        energy = input_int("Введите енергию: ")
        chastota = input_int("Введите частоту: ")

        return cls(name, energy, chastota, positive, negative, needs)

    def to_dict(self):
        skill_dict = {
            'class': 'skill',
            'name': self.name,
            'energy': self.energy,
            'chastota': self.chastota,
            'positive': self.positive_to_dict(),
            'negative': self.negative_to_dict(),
            'needs': self.needs_to_dict()
        }
        return skill_dict

    def positive_to_dict(self):
        lst = []
        for sub_skill in self.positive:
            lst.append(sub_skill.to_dict())
        return lst

    def negative_to_dict(self):
        lst = []
        for sub_skill in self.negative:
            lst.append(sub_skill.to_dict())
        return lst

    def needs_to_dict(self):
        lst = []
        for need in self.needs:
            lst.append(need.to_dict())
        return lst


class SubSkill:
    pass


class PositiveSubSkill(SubSkill):
    @staticmethod
    def list():
        return Heal, AttackBuff

    @classmethod
    def create_from_user(cls):
        print('0 - назад')
        sub_skill_classes = cls.list()
        for i, sub_skill_class in enumerate(sub_skill_classes):
            print(f'{i+1} - {sub_skill_class}')
        choice = int(input('Ваш выбор: '))
        if choice == 0:
            return None

        choice -= 1
        sub_skill_class = sub_skill_classes[choice]
        sub_skill = sub_skill_class.create_from_user()
        return sub_skill


class NegativeSubSkill(SubSkill):
    @staticmethod
    def list():
        return Damage, StateSetter

    @classmethod
    def create_from_user(cls):
        print('0 - назад')
        sub_skill_classes = cls.list()
        for i, sub_skill_class in enumerate(sub_skill_classes):
            print(f'{i + 1} - {sub_skill_class}')
        choice = int(input('Ваш выбор: '))
        if choice == 0:
            return None

        choice -= 1
        sub_skill_class = sub_skill_classes[choice]
        sub_skill = sub_skill_class.create_from_user()
        return sub_skill


class Heal(PositiveSubSkill):
    def __init__(self, hp):
        self.hp = hp

    @classmethod
    def create_from_user(cls):
        print("Создание подумения:")
        hp = int(input("Введите здоровье: "))
        return cls(hp)

    def to_dict(self):
        return {
            'class': 'Heal',
            'hp': self.hp
        }


class Buff(PositiveSubSkill):
    pass


class AttackBuff(Buff):
    def __init__(self, value):
        self.value = value

    @classmethod
    def create_from_user(cls):
        print("Создание подумения:")
        value = int(input("Введите значиние усиления: "))
        return cls(value)

    def to_dict(self):
        return {
            'class': 'AttackBuff',
            'value': self.value
        }


class Damage(NegativeSubSkill):
    value: int

    def __init__(self, value):
        self.value = value

    @classmethod
    def create_from_user(cls):
        print("Создание подумения:")
        value = int(input("Введите количество урона: "))
        return cls(value)

    def to_dict(self):
        return {
            'class': 'Damage',
            'value': self.value
        }


class StateSetter(NegativeSubSkill):
    def __init__(self, state):
        self.state = state

    @classmethod
    def create_from_user(cls):
        print("Создание подумения:")
        state = State.create_from_user()
        return cls(state)

    def to_dict(self):
        return {
            'class': 'StateSetter',
            'value': self.state.to_dict()
        }


class Need:
    types = ['state_on_self', 'state_on_enemy']
    type: str
    states: list

    def __init__(self, type_, states):
        self.type = type_
        self.states = states

    @classmethod
    def create_from_user(cls):
        type_ = input_variant(cls.types, "Выберите тип:")
        states = []
        while True:
            print('1 - добавить состояние')
            print('2 - закончить')
            choice = input()
            if choice == "1":
                state = input_variant(State.names, "Выберите состояние: ")
                states.append(state)
            elif choice == '2':
                break
        return cls(type_, states)

    def to_dict(self):
        return {
            'class': 'Need',
            'type': self.type,
            'states': self.states
        }
