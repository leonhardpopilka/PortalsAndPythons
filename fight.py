from character import Character, Attributes, Item, ItemTypes

import random

# create Items from ItemTypes
class Weapon(Item):
    pass


sigerik = Character("Sigerik", Attributes(10, 10, 10, 10, 10))
print(sigerik)

aaron = Character("Aaron", Attributes(12, 10, 8, 11, 9))
print(aaron)

print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))

