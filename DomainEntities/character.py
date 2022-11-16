# creat a RPG character with attributes and skills

import random
from typing import List


class Skills:
    def __init__(self, attack , defense, magic, stealth):
        self.attack_max = attack
        self.defense_max = defense
        self.magic_max = magic
        self.stealth_max = stealth

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


class Attributes:
    def __init__(self, strength, dexterity, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        return f"Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}, Wisdom: {self.wisdom}, Charisma: {self.charisma}"

    def __repr__(self):
        return f"Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}, Wisdom: {self.wisdom}, Charisma: {self.charisma}"

# create enum ItemTypes with Weapon, Armor, Bag and Potion
class ItemTypes:
    Weapon = 1
    Armor = 2
    Bag = 3
    Potion = 4

class Item:
    def __init__(self, name, description, type: ItemTypes, value):
        self.name = name
        self.description = description
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}"

class Character:
    def __init__(self, name, attributes: Attributes, equipment: List(Item)=[]):
        self.name = name
        self.attributes: Attributes = attributes
        self.equipped: List(Item) = equipment
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

