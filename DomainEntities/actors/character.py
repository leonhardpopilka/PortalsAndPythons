# creat a RPG character with attributes and skills
from enum import Enum
from typing import Collection
from abc import ABC, abstractmethod

from DomainEntities.skills.skills import Skill, AttackSkill, DefenseSkill, MagicSkill, StealthSkill
from DomainEntities.items.items import Item, Weapon
from .attributes import Attributes
from .status import Status


class ActorTypes(Enum):
    CHARACTER = 1
    NSC = 2
    MONSTER = 3
    SPECIAL = 4


class ActorBase(ABC):
    """An abstract class for all actors in the game"""

    @abstractmethod
    def _calculate_health(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def _set_skills_from_attributes(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass

    @abstractmethod
    def _apply_damage(self):
        pass

    @abstractmethod
    def defend_against_attack(self, attack: int) -> bool:
        pass

    @abstractmethod
    def defend_against_magic(self, magic: int) -> bool:
        pass


class Actor(ActorBase):
    """A class for all characters in the game"""

    def __init__(self,
                 name: str,
                 attributes: Attributes,
                 actor_type: ActorTypes,
                 inventory: Collection[Item],
                 ):
        self.name: str = name
        self.attributes: Attributes = attributes
        self.actor_type: ActorTypes = actor_type
        self.inventory: Collection[Item] = inventory
        self.skills: Collection[Skill] = self._set_skills_from_attributes()
        self.status: Collection[Status] = []
        self.base_health: int = self._calculate_health()
        self.current_health: int = self.base_health

    def attack(self, target):
        weapon = self._get_item(Weapon)
        if weapon is None:
            print(f"{self.name} has no weapon and cannot attack")
            return
        attack: AttackSkill = self._get_skill(AttackSkill)
        if target.defend_against_attack(attack.check()):
            print(f"{self.name} missed {target.name}")
        else:
            print(f"{self.name} hit {target.name} with {weapon.description}")
            target.take_damage(attack.damage(weapon))

    def _get_skill(self, skill_class) -> Skill:
        for skill in self.skills:
            if isinstance(skill, skill_class):
                return skill

    def _get_item(self, item_class):
        for item in self.inventory:
            if isinstance(item, item_class):
                return item

    def defend_against_attack(self, attack: int) -> bool:
        defense: Skill = self._get_skill(DefenseSkill)
        return defense.check() > attack

    def defend_against_magic(self, magic: int) -> bool:
        stealth = self._get_skill(StealthSkill)
        return stealth.check() > magic

    def _calculate_health(self):
        return self.attributes.strength * self.attributes.dexterity

    @property
    def is_alive(self):
        return self.current_health > 0

    def _apply_damage(self):
        print(f"{self.name} has dealt {self.attributes.strength} damage")
        return self.attributes.strength

    def _set_skills_from_attributes(self) -> Collection[Skill]:
        """Set the skills for this character based on their attributes"""
        return [
            AttackSkill(self.attributes.courage, self.attributes.strength),
            DefenseSkill(dexterity=self.attributes.dexterity),
            MagicSkill(self.attributes.courage, self.attributes.wisdom),
            StealthSkill(self.attributes.dexterity)
        ]

    def take_damage(self, damage):
        self.current_health -= damage
        print(f"{self.name} took {damage} damage and has {self.current_health} health left")

    def reset(self):
        self.current_health = self.base_health
        for status in self.status:
            status.reset()

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.base_health:
            self.current_health = self.base_health
        print(f"{self.name} healed {amount} and now has {self.current_health} health")

    def __str__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} has {self.current_health} health, {self.attributes} and\n{self.skills}" \
               f" and is carrying\n{self.inventory}"

    def __repr__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} has {self.current_health} health, {self.attributes} and\n{self.skills}" \
               f" and is carrying\n{self.inventory}"


class Character(Actor):
    """A class for all characters in the game"""

    def __init__(self,
                 name: str,
                 attributes: Attributes,
                 inventory: Collection[Item],
                 ):
        super().__init__(name, attributes, ActorTypes.CHARACTER, inventory)

