from DomainEntities.items.items import Item, ItemTypes


class Spell(Item):

    def use(self, item_user, target=None):
        pass

    def effect(self, item_user=None, target=None):
        pass

    def __init__(self, name: str, description: str, value: int, mana_cost: int):
        super().__init__(name, description, ItemTypes.SPELL, value)
        self.cost: int = mana_cost

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"Spell(name: {self.name}, description: {self.description}, " \
               f"value: {self.value} mana_cost: {self.cost})"
