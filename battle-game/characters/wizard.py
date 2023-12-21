import sys
sys.path.insert(0,"..")

from gears.armor import Armor
from gears.weapon import Weapon
from gears.spell import Spell

from characters.character import Character


class Wizard(Character):
    type = "Wizard"
    def __init__(self,name,hp,weapon:Weapon,armor:Armor,mana:int,spell:Spell):
        Character.__init__(self,name,hp,weapon,armor)
        self.mana = mana
        self.spell = spell

    def attack(self, other):
        choice = input("choice ( weapon/spell ) ->")
        
        if choice == "weapon":
            super().attack(other)
            
        if choice == "spell":
            other.hp -= self.spell.damage
            self.mana -= self.spell.mana


