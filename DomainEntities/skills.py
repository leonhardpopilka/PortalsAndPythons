import random

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
