# creat a RPG character with attributes and skills

import random
from typing import Collection, List

from .skills import Skills
from .attributes import Attributes
from .items import Item, Weapon, Armor, Bag, Potion

class Character:
    def __init__(self,
                name:str, 
                attributes: Attributes, 
                equipment: Collection[Item] = None, 
                inventory: Collection[Item] = None,
                ):
        self.name: str = name
        self.attributes: Attributes = attributes
        self.equipped = equipment
        self.inventory = inventory
        self.skills: Skills = self._set_skills_from_attributes(attributes)
        self.health = 100

    def attack(self, target):
        if target.skills.defended_against_attack(self.skills.attack()):
            print(f"{self.name} missed {target.name}")
        else:
            print(f"{self.name} hit {target.name}")
            target._take_damage(self.apply_damage())
    
    def _apply_damage(self):
        return self.attributes.strength

    def _set_skills_from_attributes(self, attributes: Attributes) -> Skills:
        return Skills(attributes.strength, attributes.dexterity, attributes.intelligence, attributes.wisdom)

    def _take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        """Return a string representation of this character with Attributes and Skills"""
        return f"{self.name} has {self.health} health, {self.attributes}, and {self.skills}"

    def __repr__(self):
        return self.name

