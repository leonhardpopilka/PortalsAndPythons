import random
from abc import ABC, abstractmethod
from typing import TypeVar

from DomainEntities.items.items import Item


class Skill(ABC):
    """An abstract class for all skills in the game"""

    @abstractmethod
    def check(self, modifier: int = 0) -> int:
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


SkillTypeVar = TypeVar("SkillTypeVar", bound=Skill)


class AttackSkill(Skill):
    """A class for all attack skills in the game"""

    def __init__(self, courage: int, strength: int):
        self.courage: int = courage
        self.strength: int = strength

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.courage) + modifier

    def damage(self, weapon: Item) -> int:
        return random.randint(0, self.strength + weapon.value)

    def __str__(self):
        return "Attack"

    def __repr__(self):
        return f"Attack(courage: {self.courage}, strength: {self.strength})"


class DefenseSkill(Skill):
    """A class for defense against attacks"""

    def __init__(self, dexterity: int):
        self.dexterity: int = dexterity

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.dexterity) + modifier

    def __str__(self):
        return "Defense"

    def __repr__(self):
        return f"Defense(dexterity: {self.dexterity})"


class MagicSkill(Skill):
    """A class for all magic skills in the game"""

    def __init__(self, courage: int, wisdom: int):
        self.courage: int = courage
        self.wisdom: int = wisdom

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.courage) + modifier

    def effect(self, spell: Skill) -> int:
        return random.randint(0, self.wisdom) + spell.check()

    def __str__(self):
        return "Magic"

    def __repr__(self):
        return f"Magic(courage: {self.courage})"


class StealthSkill(Skill):
    """A class for all stealth skills in the game"""

    def __init__(self, dexterity: int):
        self.dexterity: int = dexterity

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.dexterity) + modifier

    def __str__(self):
        return "Stealth"

    def __repr__(self):
        return f"Stealth(dexterity: {self.dexterity})"
