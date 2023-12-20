from characters.character import Character
from characters.barbarian import Barbarian
from gears.weapon import Weapon
from gears.weapon import weapon_list
from gears.armor import Armor
from gears.armor import armor_list
import random

from arena import Arena

randomWeapon1 = random.randrange(0,len(weapon_list)-1)
randomWeapon2 = random.randrange(0,len(weapon_list)-1)

randomArmor1 = random.randrange(0,len(armor_list)-1)
randomArmor2 = random.randrange(0,len(armor_list)-1)

weapon1 = Weapon(weapon_list[randomWeapon1]['nom'], weapon_list[randomWeapon1]['puissance'])
weapon2 = Weapon(weapon_list[randomWeapon2]['nom'], weapon_list[randomWeapon2]['puissance'])

armor1 = Armor(armor_list[randomArmor1]['nom'], armor_list[randomArmor1]['defense'])
armor2 = Armor(armor_list[randomArmor2]['nom'], armor_list[randomArmor2]['defense'])

player1 = Barbarian("player 1", 100, weapon1,armor1)
player2 = Character("player 2", 100, weapon2,armor2)

arena = Arena(player1,player2)
winner = arena.fight()

print(winner)
