from abc import ABC, abstractmethod
from typing import Callable, Any

from DomainEntities.items.items import Item, Effect, ItemTypes


class Spell(Item, ABC):

    def __init__(self, name: str, description: str, value: int, mana_cost: int):
        super().__init__(name, description, ItemTypes.SPELL, value)
        self.cost: int = mana_cost

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"Spell(name: {self.name}, description: {self.description}, " \
               f"value: {self.value} mana_cost: {self.cost})"


class Fireball(Spell):

    def __init__(self, name: str, description: str, value: int, mana_cost: int):
        super().__init__(name, description, value, mana_cost)

    def use(self, item_user, target):
        pass

    def effect(self) -> Callable[[Any], None]:
        pass
