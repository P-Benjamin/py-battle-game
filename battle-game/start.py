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
import os

class Start:
    list_player:Character = []
    loadSave = False
    
    def __init__(self) -> None:
        pass

    def menu(self):
        choice = self.welcome()

        if(int(choice) == 1):
            self.generate_random_battle()
        
        if(int(choice) == 2):
            self.generate_ordi_battle()
        
        if(int(choice) == 3):
            self.generate_pvp_battle()
        
        if(int(choice) == 4):
            self.load_data()

    def welcome(self):
        print("\n------------------------------")
        print("   Bienvenue sur BattleGame   ")
        print("------------------------------\n")

        print("Que voulez-vous faire : \n")
        print("1 - Generez bataille aléatoire")
        print("2 - Bataille contre ordi")
        print("3 - Joueur contre joueur")
        print("4 - Aventure")
        choice = ""
        while(choice not in ["1","2","3","4"]):
            choice = input("Choix : ")
        os.system('cls')
        return choice
    
    def load_data(self):
        os.system('cls')

        print("Que voulez vous faire ?")
        print(" 1 - Commencer une nouvelle partie")
        print(" 2 - Charger une partie")
        choice = ""
        while(choice not in ["1","2"]):
            choice = input("Votre choix : ")
        if(choice == "1"):
            print("Créez votre personnage")
            player =  self.create_character()
            self.list_player.append(player)
        if(choice == "2"):
            if(os.path.exists("save/map_save.pickle")):
                player =  self.generate_random_character(1)
                self.list_player.append(player)
                self.loadSave = True   
            else:
                print("Aucune partie trouvée")
                print("Créez votre personnage")
                player = self.create_character()
                self.list_player.append(player)
    

    def generate_random_battle(self) -> list:
        player1 = self.generate_random_character(1)
        player2 = self.generate_random_character(2)

        self.list_player = [player1, player2]


    def generate_random_character(self, player_id:int):
        randomType1 =  random.randrange(0,len(type_list))

        randomWeapon1 = random.randrange(0,len(weapon_list))

        randomArmor1 = random.randrange(0,len(armor_list))

        randomSpell1 = random.randrange(0,len(spell_list))

        weapon1 = Weapon(weapon_list[randomWeapon1]['name'], weapon_list[randomWeapon1]['damage'])

        armor1 = Armor(armor_list[randomArmor1]['name'], armor_list[randomArmor1]['defense'])

        spell1  = Spell(spell_list[randomSpell1]['name'], spell_list[randomSpell1]['damage'],spell_list[randomSpell1]['mana'],spell_list[randomSpell1]['type_sort'])

        if(type_list[randomType1]['name'] != 'Wizard'):
            player = globals()[type_list[randomType1]['name']](f"player {player_id}", type_list[randomType1]['hp'], weapon1,armor1)
        else: 
            player = globals()[type_list[randomType1]['name']](f"player {player_id}", type_list[randomType1]['hp'], weapon1,armor1,type_list[randomType1]['mana'],spell1, True)

        return player
    

    def generate_ordi_battle(self):
        ordi = self.generate_random_character(1)
        player = self.create_character()
        self.list_player = [ordi, player]
        

    def generate_pvp_battle(self):
        player1 = self.create_character()
        player2 = self.create_character()
        self.list_player = [player1, player2]


    def create_character(self):
        name = input("Votre nom : ")

        print("\n-----------------------")
        print("Choisissez une classe :\n")
        i = 1
        type_option = ["1"]
        for character_class in type_list:
            print(f" {i} - {character_class['name']} ")
            i += 1
            type_option.append(str(i))
        c_type = ""
        while(c_type not in type_option):
            c_type = input("Votre choix : ")

        print("\n-----------------------")
        print("Choisissez une Arme :\n")
        i = 1
        weapon_option = ["1"]
        for weapon in weapon_list:
            print(f" {i} - {weapon['name']} ")
            i += 1
            weapon_option.append(str(i))
        c_weapon=""
        while(c_weapon not in weapon_option):
            c_weapon = input("Votre choix : ")

        print("\n-----------------------")
        print("Choisissez une Armure :\n")
        i = 1
        armor_option = ["1"]
        for armor in armor_list:
            print(f" {i} - {armor['name']} ")
            i += 1
            armor_option.append(str(i))
        c_armor = ""
        while(c_armor not in armor_option):
            c_armor = input("Votre choix : ")

        if(c_type =="3"):
            print("\n-----------------------")
            print("Choisissez un sort :\n")
            i = 1
            spell_option = ["1"]
            for spell in spell_list:
                print(f" {i} - {spell['name']} ")
                i += 1
                spell_option.append(str(i))
            c_spell = ""
            while(c_spell not in spell_option):
                c_spell = input("Votre choix : ")
        
        os.system('cls')

        if (type_list[int(c_type) - 1]['name'] != 'Wizard' ):
            return globals()[type_list[int(c_type) - 1]['name']](name, type_list[int(c_type) - 1]['hp'],Weapon(weapon_list[int(c_weapon) -1 ]['name'],weapon_list[int(c_weapon) -1 ]['damage']),Armor(armor_list[int(c_armor) - 1]['name'], armor_list[int(c_armor) - 1]['defense']))
        else:
            return globals()[type_list[int(c_type) - 1]['name']](name, type_list[int(c_type) - 1]['hp'],Weapon(weapon_list[int(c_weapon) -1 ]['name'],weapon_list[int(c_weapon) -1 ]['damage']),Armor(armor_list[int(c_armor) - 1]['name'], armor_list[int(c_armor) - 1]['defense']),type_list[int(c_type) -1 ]['mana'],Spell(spell_list[int(c_spell) -1 ]["name"],spell_list[int(c_spell) -1 ]["damage"],spell_list[int(c_spell) -1 ]["mana"],spell_list[int(c_spell) -1 ]["type_sort"]), False )

    



