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
            self.GenerateRandomBattle()
        
        if(int(choice) == 2):
            self.generateOrdiBattle()
        
        if(int(choice) == 3):
            self.generatePvpBattle()


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
            player = globals()[type_list[randomType1]['nom']]("player 1", type_list[randomType1]['hp'], weapon1,armor1)
        else: 
            player = globals()[type_list[randomType1]['nom']]("player 1", type_list[randomType1]['hp'], weapon1,armor1,type_list[randomType1]['mana'],spell1)

        return player
    

    def generateOrdiBattle(self):
        ordi = self.generateRandomCharacter()
        player = self.createCharacter()
        self.list_player = [ordi, player]
        

    def generatePvpBattle(self):
        player1 = self.createCharacter()
        player2 = self.createCharacter()
        self.list_player = [player1, player2]


    def createCharacter(self):
        name = input("Votre nom : ")
        print("\n-----------------------")
        print("Choisissez une classe :\n")
        i = 1
        for character_class in type_list:
            print(f" {i} - {character_class['nom']} ")
            i += 1
        c_type = input("Votre choix : ")

        print("\n-----------------------")
        print("Choisissez une Arme :\n")
        i = 1
        for weapon in weapon_list:
            print(f" {i} - {weapon['nom']} ")
            i += 1
        c_weapon = input("Votre choix : ")

        print("\n-----------------------")
        print("Choisissez une Armure :\n")
        i = 1
        for armor in armor_list:
            print(f" {i} - {armor['nom']} ")
            i += 1
        c_armor = input("Votre choix : ")

        return globals()[type_list[int(c_type) - 1]['nom']](name, type_list[int(c_type) - 1]['hp'],Weapon(weapon_list[int(c_weapon) -1 ]['nom'],weapon_list[int(c_weapon) -1 ]['puissance']),Armor(armor_list[int(c_armor) - 1]['nom'], armor_list[int(c_armor) - 1]['defense']))
        




