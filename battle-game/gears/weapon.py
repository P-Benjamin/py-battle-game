weapon_list = [
    {"nom": "Épée", "puissance": 10},
    {"nom": "Hache", "puissance": 15},
    {"nom": "Arc", "puissance": 8},
    {"nom": "Marteau", "puissance": 12},
    {"nom": "Dague", "puissance": 7}
]
class Weapon:

    def __init__(self,name:str,damage:int):
        self.name = name
        self.damage = damage
    
