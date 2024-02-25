armor_list = [
    {"name": "Armure légère", "defense": 5},
    {"name": "Armure lourde", "defense": 10},
    {"name": "Robe magique", "defense": 3},
    {"name": "Casque en acier", "defense": 6},
    {"name": "Bouclier de bois", "defense": 4}
]
monster_armor = {"name" : "Skin", "defense" : 2}
class Armor:

    def __init__(self,name:str,defense:int):
        self.name = name
        self.defense = defense
    
