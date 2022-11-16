from DomainEntities.actors.character import Character
from DomainEntities.actors.attributes import Attributes
from DomainEntities.items.items import Weapon

if __name__ == "__main__":
    sharp_sword = Weapon("Sword", "A sharp sword.", 4)
    blunt_sword = Weapon("Sword", "A blunt sword.", 1)
    sigerik = Character("Sigerik", Attributes(10, 10, 10, 10), [sharp_sword])
    print(sigerik)

    aaron = Character("Aaron", Attributes(12, 10, 8, 11), [blunt_sword])
    print(aaron)
    
    round = 1
    while sigerik.is_alive and aaron.is_alive:
        print(f"\nRound {round}")
        sigerik.attack(aaron)
        aaron.attack(sigerik)
        round += 1



