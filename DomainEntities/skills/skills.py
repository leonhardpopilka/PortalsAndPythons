import random
from abc import ABC, abstractmethod
from DomainEntities.actors.attributes import Attributes

class BaseSkills(ABC):
    """An abstract class for all skills in the game"""

    def __init__(self, attributes: Attributes):
        self.attack_max = attributes.strength
        self.defense_max = attributes.dexterity
        self.magic_max = attributes.courage
        self.stealth_max = attributes.wisdom

    def __str__(self):
        return f"Attack: {self.attack_max}, Defense: {self.defense_max}, Magic: {self.magic_max}, Stealth: {self.stealth_max}"

    def attack(self):
        return random.randint(0, self.attack_max)

    def defense(self):
        return random.randint(0, self.defense_max)

    def magic(self):
        return random.randint(0, self.stealth_max)

    def stealth(self, max):
        return random.randint(0, max)

    def defended_against_attack(self, attack: int) -> bool:
        return self.defense() >= attack

    def defended_against_magic(self, magic: int) -> bool:
        return self.stealth() >= magic

class Skills(BaseSkills):
    def __init__(self, attributes: Attributes):
        super().__init__(attributes=attributes)