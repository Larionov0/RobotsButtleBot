from Tools.main import input_int
from .skills import *
from json import dumps, load


class CreaturePrototype:
    def __init__(self, name, hp, energy, energy_recovery, hp_recovery, skills):
        self.name = name
        self.hp = hp
        self.energy = energy
        self.energy_recovery = energy_recovery
        self.hp_recovery = hp_recovery
        self.skills = skills


class Creature(CreaturePrototype):
    """
    + name: str
    + max_hp: int
    + hp: int
    + max_energy: int
    + energy: int
    + energy_recovey: int
    + hp_recovery: int
    + skills: list[Skill]
    """

    def __init__(self, name, hp, energy, energy_recovery, hp_recovery, skills):
        super().__init__(name, hp, energy, energy_recovery, hp_recovery, skills)
        self.max_hp = hp
        self.max_energy = energy


class HeroPrototype(CreaturePrototype):
    def __init__(self, name, hp, energy, energy_recovery, hp_recovery, skills, satiety):
        super().__init__(name, hp, energy, energy_recovery, hp_recovery, skills)
        self.satiety = satiety

    @classmethod
    def create_from_user(cls):
        name = input("Введите имя нового персонажа: ")
        hp = input_int("Введите HP персонажа: ")
        energy = input_int("Введите energy персонажа: ")
        energy_recovery = input_int("Введите energy_recovery персонажа: ")
        hp_recovery = input_int("Введите hp_recovery персонажа: ")
        satiety = input_int("Введите satiety персонажа: ")

        skills = Skill.create_skills()

        hero = cls(name, hp, energy, energy_recovery, hp_recovery, skills, satiety)
        return hero

    def to_dict(self):
        """
        {
        'name': 'Klava',
        "hp": 12,
        ...
        'skills': [{}, {}, {}]
        }
        :return:
        """
        hero_dict = {}
        for attr in "name", 'hp', 'energy', 'energy_recovery', 'hp_recovery', 'satiety':
            hero_dict[attr] = getattr(self, attr)

        skills = self.skills_to_dict()
        hero_dict['skills'] = skills
        hero_dict['class'] = 'Hero'
        return hero_dict

    def skills_to_dict(self):
        skills = []
        for skill in self.skills:
            skills.append(skill.to_dict())
        return skills


class NPCPrototype(CreaturePrototype):
    pass


class Hero(HeroPrototype, Creature):
    def __init__(self, name, hp, energy, energy_recovery, hp_recovery, skills, satiety):
        Creature.__init__(self, name, hp, energy, energy_recovery, hp_recovery, skills)
        self.satiety = satiety
        self.max_satiety = satiety


class NPC:
    pass

