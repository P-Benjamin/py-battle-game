import sys
import random

sys.path.insert(0,"..")

from gears.armor import Armor
from gears.weapon import Weapon
from gears.spell import Spell

from characters.character import Character

from characters.character_type import type_list

random_attack = { 1 : "weapon", 2 : "spell"} 
class Wizard(Character):
    type = "Wizard"
    def __init__(self,name,hp,weapon:Weapon,armor:Armor,mana:int,spell:Spell, random:bool, defense = type_list[2]['defense']):
        Character.__init__(self,name,hp,weapon,armor,defense,mana)
        self.mana = mana
        self.spell = spell
        self.random = random

    def attack(self, other):
        if(self.random):
           random_choice =  random.randint(1,2)
           choice = random_attack[random_choice]
        else:
            choice = ""
            while(choice != "weapon" and choice != "spell"):
                choice = input("Choix ( weapon/spell ) -> ")
        
        if choice == "weapon":
            super().attack(other)
            
        if choice == "spell":
            print(f"{self.name} ({self.type}) attaque avec {self.spell.name} ({self.spell.damage}) {other.name} ({other.type}) equipé de {other.armor.name} ({other.armor.defense})")
            if(self.mana <= 0 or self.mana - self.spell.mana < 0 ):
                print(f"{self.type} n\'a plus assez ne mana pour ce sort et ne peut pas attaquer")
                super().attack(other)
            else:
                if(self.spell.type == "heal"):
                    self.hp += self.spell.damage
                elif(self.spell.type == "protection"):
                    self.armor.defense += self.spell.damage
                else:
                    other.hp -= self.spell.damage
                self.mana -= self.spell.mana


