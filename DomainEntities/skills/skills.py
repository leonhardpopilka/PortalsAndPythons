import random
from abc import ABC, abstractmethod
from DomainEntities.items.items import Item

class Skill(ABC):
    """An abstract class for all skills in the game"""

    @abstractmethod
    def check(self, value: int) -> int:
        pass


class AttackSkill(Skill):
    """A class for all attack skills in the game"""

    def __init__(self, courage: int, strength: int):
        self.courage: int = courage
        self.strength: int = strength

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.courage) + modifier
    
    def damage(self, weapon: Item) -> int:
        return random.randint(0, self.strength + weapon.value)

class DefenseSkill(Skill): 
    """A class for defense against attacks"""

    def __init__(self, dexterity: int):
        self.dexterity: int = dexterity

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.dexterity) + modifier

class MagicSkill(Skill):
    """A class for all magic skills in the game"""

    def __init__(self, courage: int):
        self.courage : int = courage

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.courage) + modifier

class StealthSkill(Skill):
    """A class for all stealth skills in the game"""

    def __init__(self, dexterity: int):
        self.dexterity: int = dexterity

    def check(self, modifier: int = 0) -> int:
        return random.randint(0, self.dexterity) + modifier

# class BaseSkills(ABC):
#     """An abstract class for all skills in the game"""

#     def __init__(self, attributes: Attributes):
#         self.attack_max = attributes.strength
#         self.defense_max = attributes.dexterity
#         self.magic_max = attributes.courage
#         self.stealth_max = attributes.wisdom

#     def __str__(self):
#         return f"Attack: {self.attack_max}, Defense: {self.defense_max}, Magic: {self.magic_max}, Stealth: {self.stealth_max}"


#     def defended_against_attack(self, attack: int) -> bool:
#         return self.defense() >= attack

#     def defended_against_magic(self, magic: int) -> bool:
#         return self.stealth() >= magic

