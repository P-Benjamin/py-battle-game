from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from arena import Arena

weapon = Weapon("arme1", 10)
armor = Armor("armor1",10)

player1 = Character("player 1", 100, weapon,armor)
player2 = Character("player 2", 100, weapon,armor)

arena = Arena(player1,player2)
winner = arena.fight()

print(winner)
