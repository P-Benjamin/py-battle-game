from characters.character import Character
import os
class Arena:
    def __init__(self,first_character:Character, second_character:Character):
        self.first_character = first_character
        self.second_character = second_character
    
    def displayResult(self):
        print("Results: ")
        print(self.first_character.name, self.first_character.hp, "HP")
        print(self.second_character.name, self.second_character.hp, "HP")
        input("------------------")

    def fight(self) -> str:
        self.presentation()
        while self.first_character.hp > 0 and self.second_character.hp > 0:
            self.first_character.attack(self.second_character)

            self.displayResult()
            
            if self.second_character.hp <= 0:
                break
            
            self.second_character.attack(self.first_character)

            self.displayResult()
            
        winner =   self.first_character.name if self.first_character.hp > 0 else self.second_character.name
        return winner
    
    def presentation(self):
        print("Name            " + "{:<40}".format(self.first_character.name) + self.second_character.name)
        print("Type            " + "{:<40}".format(self.first_character.type) + self.second_character.type)
        print("Vie             " + "{:<40}".format(self.first_character.hp) + f"{self.second_character.hp}")
        print("Arme(dmg)       " + "{:<25}".format(self.first_character.weapon.name+f"({self.first_character.weapon.damage})") +"{:<15}".format("VS") + self.second_character.weapon.name+f"({self.second_character.weapon.damage})")
        print("Armure          " + "{:<40}".format(self.first_character.armor.name+f"({self.first_character.armor.defense})") + self.second_character.armor.name+f"({self.second_character.armor.defense})")
        print("Defense         " + "{:<40}".format(self.first_character.defense) + f"{self.second_character.defense}")
        print("Mana            " + "{:<40}".format(self.first_character.mana) + f"{self.second_character.mana}")

        input("Appuyez sur Entrée pour commencer le combat")
        os.system('cls')
    

