weapon_list = [
    {"nom": "Épée", "puissance": 10},
    {"nom": "Hache", "puissance": 15},
    {"nom": "Arc", "puissance": 8},
    {"nom": "Marteau", "puissance": 12},
    {"nom": "Dague", "puissance": 7}
]

monster_attack = {"Orc" : {"name" : "Orc Attack", "damage" : 10},
                  "Goblin" :{"name" : "Goblin Attack", "damage" : 6},
                  "Skeleton": {"name" : "Skeleton Attack", "damage" : 4},
                  "Giant Spider": {"name" : "Spider Attack", "damage" : 7}}
class Weapon:

    def __init__(self,name:str,damage:int):
        self.name = name
        self.damage = damage
    
