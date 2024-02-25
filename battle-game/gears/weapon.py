weapon_list = [
    {"name": "Épée", "damage": 10},
    {"name": "Hache", "damage": 15},
    {"name": "Arc", "damage": 8},
    {"name": "Marteau", "damage": 12},
    {"name": "Dague", "damage": 7}
]

monster_attack = {"Orc" : {"name" : "Orc Attack", "damage" : 10},
                  "Goblin" :{"name" : "Goblin Attack", "damage" : 6},
                  "Skeleton": {"name" : "Skeleton Attack", "damage" : 4},
                  "Giant Spider": {"name" : "Spider Attack", "damage" : 7}}
class Weapon:

    def __init__(self,name:str,damage:int):
        self.name = name
        self.damage = damage
    
