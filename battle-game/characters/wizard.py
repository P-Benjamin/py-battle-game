import sys
sys.path.insert(0,"..")

from gears.armor import Armor
from gears.weapon import Weapon
from gears.spell import Spell

from character import Character


class Wizard(Character):
    type = "Wizard"
    def __init__(self,name,hp,weapon:Weapon,armor:Armor,mana,spell:Spell):
        Character(name,hp,weapon,armor)
        self.mana = mana
        self.spell = spell

    def attack(self, other, choice):
        if choice == "weapon":
            super().attack(other)
        if choice == "sort":
            other.hp -= self.spell.damage
            self.mana -= self.sorts.mana


