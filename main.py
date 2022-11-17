from DomainEntities.actors.character import Character
from DomainEntities.actors.attributes import Attributes
from DomainEntities.items.items import Weapon


def determine_winner(a: Character, b: Character):
    if not a.is_alive and b.is_alive:
        return b
    elif not b.is_alive and a.is_alive:
        return a
    else:
        return None


if __name__ == "__main__":
    sharp_sword = Weapon("Sword", "a sharp sword.", 1)
    blunt_sword = Weapon("Sword", "a blunt sword.", 1)

    sigerik = Character(
        "Sigerik",
        Attributes(
            courage=5,
            strength=3,
            dexterity=1,
            wisdom=1,
        ),
        [sharp_sword]
    )
    aaron = Character(
        "Aaron",
        Attributes(
            courage=3,
            strength=3,
            dexterity=3,
            wisdom=1,
        ),
        [blunt_sword]
    )

    print(sigerik)
    print(aaron)

    counter = {"Sigerik": 0, "Aaron": 0}

    for i in range(100):
        combat_round = 1
        while sigerik.is_alive and aaron.is_alive:
            print(f"\nRound {combat_round}")
            sigerik.attack(aaron)
            aaron.attack(sigerik)
            combat_round += 1
        winner = determine_winner(sigerik, aaron)
        if winner is not None:
            print(f"\n{winner.name} wins!")
            counter[winner.name] += 1
        else:
            print("\nIt's a draw!")
        sigerik.reset()
        aaron.reset()

    print(f"\nSigerik wins {counter['Sigerik']} times")
    print(f"Aaron wins {counter['Aaron']} times")
