weapon_list = [
    {"nom": "Épée", "puissance": 10},
    {"nom": "Hache", "puissance": 15},
    {"nom": "Arc", "puissance": 8},
    {"nom": "Marteau", "puissance": 12},
    {"nom": "Dague", "puissance": 7}
]

monster_attack = {"Orc" : {"name" : "Orc Attack", "damage" : 13},
                  "Goblin" :{"name" : "Goblin Attack", "damage" : 8},
                  "Skeleton": {"name" : "Skeleton Attack", "damage" : 6},
                  "Giant Spider": {"name" : "Spider Attack", "damage" : 10}}
class Weapon:

    def __init__(self,name:str,damage:int):
        self.name = name
        self.damage = damage
    
