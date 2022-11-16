from DomainEntities.character import Character
from DomainEntities.attributes import Attributes
# from .DomainEntities.skills import Skills
# from .DomainEntities.items import Item, Weapon, Armor, Bag, Potion

sigerik = Character("Sigerik", Attributes(10, 10, 10, 10, 10))
print(sigerik)

aaron = Character("Aaron", Attributes(12, 10, 8, 11, 9))
print(aaron)

print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))

