from character import Character

class Barbarian(Character):
    def __init__(self,name,hp,weapon,armor):
        Character(name,hp,weapon,armor)


    def attack(self, other):
         super().attack(other)
         super().attack(other)

