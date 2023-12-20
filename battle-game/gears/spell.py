spell_list = [
    {"name": "Boule de feu", "type_sort": "degats", "damage": 15, "mana": 10},
    {"name": "Soin léger", "type_sort": "heal", "damage": 10, "mana": 8},
    {"name": "Bouclier magique", "type_sort": "protection", "damage": 5, "mana": 5},
]
class Spell:
    def __init__(self,name, damage,mana,type):
        self.name = name
        self.damage = damage
        self.mana = mana
        self.type = type
