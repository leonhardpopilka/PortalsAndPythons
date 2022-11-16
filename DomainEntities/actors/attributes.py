class Attributes:
    def __init__(self, courage: int, wisdom: int, dexterity: int, strength: int):
        self.courage = courage
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.strength = strength

    def __str__(self):
        return f"Strength: {self.strength}, Dexterity: {self.dexterity}, Courage: {self.courage}, Wisdom: {self.wisdom}."

    def __repr__(self):
        return f"Strength: {self.strength}, Dexterity: {self.dexterity}, Courage: {self.courage}, Wisdom: {self.wisdom}."
