from DomainEntities.actors.character import Character
from DomainEntities.actors.attributes import Attributes

if __name__ == "__main__":
    sigerik = Character("Sigerik", Attributes(10, 10, 10, 10), [])
    print(sigerik)

    aaron = Character("Aaron", Attributes(12, 10, 8, 11), [])
    print(aaron)
    
    round = 1
    while sigerik.is_alive and aaron.is_alive:
        print(f"\nRound {round}")
        sigerik.attack(aaron)
        aaron.attack(sigerik)
        round += 1



