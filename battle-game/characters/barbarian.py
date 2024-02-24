from characters.character import Character
from characters.character_type import type_list

class Barbarian(Character):
    type = "Barbarian"

    def __init__(self,name,hp,weapon,armor,defense = type_list[1]['defense']):
        Character.__init__(self,name,hp,weapon,armor,defense)


    def attack(self, other):
         super().attack(other)
         super().attack(other)

