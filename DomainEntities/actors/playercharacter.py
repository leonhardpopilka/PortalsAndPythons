# creat an RPG character with attributes and skills
from abc import ABC, abstractmethod
from enum import Enum
from typing import Collection, TypeVar

from DomainEntities.items.items import Item, Weapon, ItemTypeVar
from DomainEntities.skills.skills import Skill, AttackSkill, DefenseSkill, MagicSkill, StealthSkill, \
    SkillTypeVar
from .attributes import Attributes
from .status import Status
from ..items.spells import Spell


class ActorTypes(Enum):
    PC = 1
    NSC = 2
    MONSTER = 3
    SPECIAL = 4


class CharacterClasses(Enum):
    WARRIOR = 1
    MAGE = 2
    NONE = 0


class ActorBase(ABC):
    """An abstract class for all actors in the game"""

    @property
    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def attack(self, target: 'ActorBase'):
        pass

    @abstractmethod
    def defend_against_attack(self, attack: int) -> bool:
        pass

    @abstractmethod
    def heal(self, amount: int):
        pass

    @abstractmethod
    def take_damage(self, amount: int):
        pass

    @abstractmethod
    def cast(self, spell: Skill, target: 'ActorBase'):
        pass

    @abstractmethod
    def defend_against_magic(self, magic: int) -> bool:
        pass

    @abstractmethod
    def gain_mana(self, amount: int):
        pass

    @abstractmethod
    def spent_mana(self, amount: int) -> bool:
        pass

    @abstractmethod
    def reset(self):
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
        self.base_mana: int = 0
        self.current_mana: int = 0

    @property
    def is_alive(self):
        return self.current_health > 0

# Public methods
    def attack(self, target: 'Actor', weapon: Weapon = None):
        used_weapon: Weapon = weapon if weapon else self._get_item(Weapon)
        if used_weapon is None:
            print(f"{self.name} has no weapon and cannot attack")
            return
        attack: AttackSkill = self._get_skill(AttackSkill)
        if target.defend_against_attack(attack.check()):
            print(f"{self.name} missed {target.name}")
        else:
            print(f"{self.name} hit {target.name} with {used_weapon.description}")
            target.take_damage(attack.damage(used_weapon))

    def cast(self, spell: Spell, target: 'Actor'):
        if self.current_mana < spell.cost:
            print(f"{self.name} does not have enough mana to cast that spell")
            return
        magic: MagicSkill = self._get_skill(MagicSkill)
        if target.defend_against_magic(magic.check()):
            print(f"{self.name}'s spell missed {target.name}")
        else:
            print(f"{self.name} casted '{spell.name}' on {target.name}")
            target.apply_effect(spell.effect())
            self.spent_mana(spell.cost)

    def defend_against_attack(self, attack: int) -> bool:
        defense: DefenseSkill = self._get_skill(DefenseSkill)
        return defense.check() > attack

    def defend_against_magic(self, magic: int) -> bool:
        stealth: StealthSkill = self._get_skill(StealthSkill)
        return stealth.check() > magic

    def take_damage(self, amount):
        self.current_health -= amount
        print(f"{self.name} took {amount} damage and has {self.current_health} health left")

    def heal(self, amount: int):
        self.current_health += amount
        if self.current_health > self.base_health:
            self.current_health = self._calculate_health()
        print(f"{self.name} healed {amount} and now has {self.current_health} health")

    def gain_mana(self, amount: int):
        self.current_mana += amount
        if self.current_mana > self.base_mana:
            self.current_mana = self._calculate_mana()
        print(f"{self.name} gained {amount} and now has {self.current_mana} mana")

    def spent_mana(self, amount: int) -> bool:
        if self.current_mana < amount:
            print(f"{self.name} does not have enough mana to cast that spell")
            return False
        self.current_mana -= amount
        print(f"{self.name} spent {amount} and now has {self.current_mana} mana")
        return True

    def reset(self):
        self.current_health = self._calculate_health()
        self.current_mana = self._calculate_mana()
        for status in self.status:
            status.reset()

# Private methods
    def _set_skills_from_attributes(self) -> Collection[Skill]:
        """Set the skills for this character based on their attributes"""
        return [
            AttackSkill(self.attributes.courage, self.attributes.strength),
            DefenseSkill(dexterity=self.attributes.dexterity),
            MagicSkill(self.attributes.courage, self.attributes.wisdom),
            StealthSkill(self.attributes.dexterity)
        ]

    def _get_skill(self, skill_class) -> SkillTypeVar:
        for skill in self.skills:
            if isinstance(skill, skill_class):
                return skill

    def _get_item(self, item_class) -> ItemTypeVar:
        for item in self.inventory:
            if isinstance(item, item_class):
                return item

    def _calculate_health(self):
        return self.attributes.strength * self.attributes.dexterity

    def _calculate_mana(self):
        if isinstance(self, PlayerCharacter) or isinstance(self, NonPlayerCharacter):
            if self.character_class != CharacterClasses.MAGE:
                return 0
        return self.attributes.wisdom * self.attributes.courage

    def __str__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} has {self.current_health} health, {self.attributes} and\n{self.skills}" \
               f" and is carrying\n{self.inventory}"

    def __repr__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} has {self.current_health} health, {self.attributes} and\n{self.skills}" \
               f" and is carrying\n{self.inventory}"


class PlayerCharacter(Actor):
    """A class for all player-characters in the game"""

    def __init__(self,
                 name: str,
                 character_class: CharacterClasses,
                 attributes: Attributes,
                 inventory: Collection[Item],
                 ):
        super().__init__(name, attributes, ActorTypes.PC, inventory)
        self.character_class: CharacterClasses = character_class
        self._exp: int = 0
        self.base_mana = self._calculate_mana()
        self.current_mana = self.base_mana

    @property
    def exp(self):
        return self._exp

    def add_exp(self, amount):
        self._exp += amount
        print(f"{self.name} gained {amount} experience and now has {self._exp} experience")

    def __str__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} (XP: {self.exp}) has {self.current_health} health and " \
               f"{self.current_mana} mana, {self.attributes} and\n{self.skills}" \
               f" and is carrying\n{self.inventory}"

    def __repr__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} (XP: {self.exp}) has {self.current_health} health and " \
               f"{self.current_mana} mana, {self.attributes} and\n{self.skills}" \
               f" and is carrying\n{self.inventory}"


class NonPlayerCharacter(Actor):
    """A class for all non-player-characters in the game"""

    def __init__(self,
                 name: str,
                 character_class: CharacterClasses,
                 attributes: Attributes,
                 inventory: Collection[Item],
                 ):
        super().__init__(name, attributes, ActorTypes.NSC, inventory)
        self.character_class: CharacterClasses = character_class
        self.base_mana = self._calculate_mana()
        self.current_mana = self.base_mana


ActorTypeVar = TypeVar('ActorTypeVar', bound=Actor)
