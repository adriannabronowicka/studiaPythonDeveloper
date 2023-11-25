"""
Utwórz klasę:
Player / Hero
- self.hp
- self.damage
- def attack
Monster / NPC / Attackable
- self.hp
- self.damage
 - def attack

Zasymuluj walkę 2 obiektów
Kiedy self.hp <= oznacz obiekt jako martwy
Ogłoś zwycięzce pojedynku
"""

class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        if not self.is_alive:
            print(f"{self.name} can't attack because it's already dead")
            return
        target.hp -= self.damage

    @property
    def is_alive(self) -> bool:
        return self.hp > 0


archer = Player("Archer", 100, 10)
dragon = Player("Dragon", 150, 10)

while archer.hp > 0 and dragon.hp > 0:
    archer.attack(dragon)
    dragon.attack(archer)
print(f"After attack Archer has {archer.hp} and Dragon has {dragon.hp}")

if dragon.hp > 0:
    print("The fight has been won by Dragon")
else:
    print("The fight has been won by Archer")

# wewnatrz klasy Player zrobic if not martwy: attack
