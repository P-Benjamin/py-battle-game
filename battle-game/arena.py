from characters.character import Character

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
        while self.first_character.hp > 0 and self.second_character.hp > 0:
            self.first_character.attack(self.second_character)

            self.displayResult()
            
            if self.second_character.hp <= 0:
                break
            
            self.second_character.attack(self.first_character)

            self.displayResult()
            
        winner =   self.first_character.name if self.first_character.hp > 0 else self.second_character.name
        return winner
    

