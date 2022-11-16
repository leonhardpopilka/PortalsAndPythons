# creat a RPG character with attributes and skills

from typing import Collection, List
from abc import ABC, abstractmethod

from DomainEntities.skills.skills import Skills
from DomainEntities.items.items import Item
from .attributes import Attributes

class ActorTypes:
    Character = 1
    NSC = 2
    Monster = 3
    Special = 4

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
    def attack(self, target):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def _take_damage(self, damage):
        pass

    @abstractmethod
    def _apply_damage(self):
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
        self.skills: Collection[Skills] = Skills(attributes=self.attributes)
        self.base_health: int = self._calculate_health()
        self.current_health: int = self.base_health

    
    def attack(self, target):
        if target.skills.defended_against_attack(self.skills.attack()):
            print(f"{self.name} missed {target.name}")
        else:
            print(f"{self.name} hit {target.name}")
            target._take_damage(self._apply_damage())

    def _calculate_health(self):
        return self.attributes.strength * self.attributes.courage
    
    @property
    def is_alive(self):
        return self.current_health > 0

    def _apply_damage(self):
        print(f"{self.name} has dealt {self.attributes.strength} damage")
        return self.attributes.strength

    def _set_skills_from_attributes(self) -> Skills:
        return Skills(courage=self.attributes.courage, 
                      wisdom=self.attributes.wisdom, 
                      dexterity=self.attributes.dexterity, 
                      strength=self.attributes.strength,
                      )

    def _take_damage(self, damage):
        self.current_health -= damage
        print(f"{self.name} took {damage} damage and has {self.current_health} health left")

    def __str__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} has {self.current_health} health, {self.attributes} and\n{self.skills}"\
        f" and is carrying\n{self.inventory}"
        

class Character(Actor):
    """A class for all characters in the game"""

    def __init__(self, 
                name: str, 
                attributes: Attributes,
                inventory: Collection[Item],
                ):
        super().__init__(name, attributes, ActorTypes.Character, inventory)

    


