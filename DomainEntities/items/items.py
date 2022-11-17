from abc import ABC
from enum import Enum
from typing import TypeVar


class ItemTypes(Enum):
    WEAPON = 1
    ARMOR = 2
    BAG = 3
    POTION = 4


class Item(ABC):
    def __init__(self, name, description, item_type: ItemTypes, value):
        self.name = name
        self.description = description
        self.type: ItemTypes = item_type
        self.value = value

    def __str__(self):
        return f"{self.name}({self.description}) Value: {self.value}"

    def __repr__(self):
        return f"{self.name}({self.description}) Value: {self.value}"


class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.WEAPON, value)


class Armor(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.ARMOR, value)


class Bag(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.BAG, value)


class Potion(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.POTION, value)


ItemTypeVar = TypeVar('ItemTypeVar', bound=Item)
