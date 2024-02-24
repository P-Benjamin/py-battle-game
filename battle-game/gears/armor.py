armor_list = [
    {"nom": "Armure légère", "defense": 5},
    {"nom": "Armure lourde", "defense": 10},
    {"nom": "Robe magique", "defense": 3},
    {"nom": "Casque en acier", "defense": 6},
    {"nom": "Bouclier de bois", "defense": 4}
]
monster_armor = {"name" : "rien", "defense" : 0}
class Armor:

    def __init__(self,name:str,defense:int):
        self.name = name
        self.defense = defense
    
