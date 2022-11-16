from DomainEntities.actors.character import Character
from DomainEntities.actors.attributes import Attributes

sigerik = Character("Sigerik", Attributes(10, 10, 10, 10), [])
print(sigerik)

aaron = Character("Aaron", Attributes(12, 10, 8, 11), [])
print(aaron)

print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))
print(sigerik.skills.defended_against_attack(aaron.skills.attack()))

