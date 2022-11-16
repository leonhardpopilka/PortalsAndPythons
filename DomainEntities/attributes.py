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
