from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor


class Monster(Character):
    type = "Monster"
    def __init__(self,name:str,hp:int, weapon:Weapon, armor:Armor,defense):
        Character.__init__(self,name,hp,weapon,armor,defense)