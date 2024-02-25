import sys
sys.path.insert(0,"..")

from gears.armor import Armor
from gears.weapon import Weapon
from characters.character_type import type_list

class Character:
    type = "Human"
    def __init__(self,name:str,hp:int, weapon:Weapon, armor:Armor, defense = type_list[0]['defense'],mana = 0):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.defense = defense
        self.armor.defense += defense
        self.mana = mana
        
    def attack(self,other):
        print(f"{self.name} ({self.type}) attaque avec {self.weapon.name} ({self.weapon.damage}) {other.name} ({other.type}) equipé de {other.armor.name} ({other.armor.defense})")
        other.hp -= self.weapon.damage - (self.weapon.damage * (other.armor.defense / 100))

if __name__ == "__main__":
    player_1 = Character("Player 1", 100, Weapon("Weapon 1", 10), Armor("Armor 1", 10))
    player_2 = Character("Player 2", 100, Weapon("Weapon 2", 10), Armor("Armor 2", 10))

    player_1.attack(player_2)

    print(player_2.hp)
                         
