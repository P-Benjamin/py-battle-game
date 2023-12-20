from characters.character import Character

class Barbarian(Character):
    type = "Barbarian"

    def __init__(self,name,hp,weapon,armor):
        Character.__init__(self,name,hp,weapon,armor)


    def attack(self, other):
         super().attack(other)
         super().attack(other)

