from characters.character import Character
from characters.barbarian import Barbarian
from characters.wizard import Wizard
from characters.character_type import type_list

from gears.weapon import Weapon
from gears.weapon import weapon_list
from gears.armor import Armor
from gears.armor import armor_list
from gears.spell import Spell
from gears.spell import spell_list

import random

class Start:
    
    list_player:Character = []
    
    def __init__(self) -> None:
        choice = self.Welcome()

        if(int(choice) == 1):
            init = self.GenerateRandomBattle()
        
    def Welcome(self):
        print("\n------------------------------")
        print("   Bienvenue sur BattleGame   ")
        print("------------------------------\n")

        print("Que voulez-vous faire : \n")
        print("1 - Generez bataille aléatoire")
        print("2 - Bataille contre ordi")
        print("3 - Joueur contre joueur")
        choice = input("Choix : ")
        return choice
    
    def GenerateRandomBattle(self) -> list:
        player1 = self.generateRandomCharacter()
        player2 = self.generateRandomCharacter()
        self.list_player = [player1, player2]


    def generateRandomCharacter(self):
        
        randomType1 =  random.randrange(0,len(type_list))

        randomWeapon1 = random.randrange(0,len(weapon_list))

        randomArmor1 = random.randrange(0,len(armor_list))

        randomSpell1 = random.randrange(0,len(spell_list))

        weapon1 = Weapon(weapon_list[randomWeapon1]['nom'], weapon_list[randomWeapon1]['puissance'])

        armor1 = Armor(armor_list[randomArmor1]['nom'], armor_list[randomArmor1]['defense'])

        spell1  = Spell(spell_list[randomSpell1]['name'], spell_list[randomSpell1]['damage'],spell_list[randomSpell1]['mana'],spell_list[randomSpell1]['type_sort'])

        if(type_list[randomType1]['nom'] != 'Wizard'):
            player = globals()[type_list[randomType1]['nom']]("player 1", 100, weapon1,armor1)
        else: 
            player = globals()[type_list[randomType1]['nom']]("player 1", 100, weapon1,armor1,100,spell1)

        return player
    
    



