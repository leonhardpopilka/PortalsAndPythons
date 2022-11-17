from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar, Callable, Any

# from DomainEntities.actors.playercharacter import ActorBase


class ItemTypes(Enum):
    WEAPON = 1
    ARMOR = 2
    BAG = 3
    POTION = 4
    SPELL = 5


class Effect:
    pass


class Item(ABC):
    def __init__(self, name, description, item_type: ItemTypes, value):
        self.name = name
        self.description = description
        self.type: ItemTypes = item_type
        self.value: int = value

    @abstractmethod
    def use(self, item_user, target):
        pass

    @abstractmethod
    def effect(self) -> Callable[[Any], None]:
        pass

    def __str__(self):
        return f"{self.name}({self.description}) Value: {self.value}"

    def __repr__(self):
        return f"{self.name}({self.description}) Value: {self.value}"


class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.WEAPON, value)

    def use(self, item_user, target):
    # def use(self, item_user: ActorBase, target: ActorBase):
        item_user.attack(target)

    def effect(self) -> Callable[[Any], None]:
        pass


class Armor(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.ARMOR, value)

    def use(self, item_user, target):
        pass

    def effect(self) -> Callable[[Any], None]:
        pass


class Bag(Item):

    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.BAG, value)

    def use(self, item_user, target):
        pass

    def effect(self) -> Callable[[Any], None]:
        pass


class Potion(Item):

    def __init__(self, name, description, value):
        super().__init__(name, description, ItemTypes.POTION, value)

    def use(self, item_user, target):
        pass

    def effect(self) -> Callable[[Any], None]:
        return lambda actor: actor.heal(self.value)


ItemTypeVar = TypeVar('ItemTypeVar', bound=Item)
