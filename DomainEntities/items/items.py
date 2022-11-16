from abc import ABC

class ItemTypes:
    Weapon = 1
    Armor = 2
    Bag = 3
    Potion = 4

class Item(ABC):
    def __init__(self, name, description, type: ItemTypes, value):
        self.name = name
        self.description = description
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}"

class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.Weapon, value)

class Armor(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.Armor, value)

class Bag(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.Bag, value)

class Potion(Item): 
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.Potion, value)