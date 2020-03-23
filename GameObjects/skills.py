class Skill:
    pass


class SubSkill:
    pass


class PositiveSubSkill(SubSkill):
    pass


class NegativeSubSkill(SubSkill):
    pass


class Heal(PositiveSubSkill):
    pass


class Buff(PositiveSubSkill):
    pass


class AttackBuff(Buff):
    pass


class Damage(NegativeSubSkill):
    pass
