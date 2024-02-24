from start import Start
from arena import Arena
import random
from bestiary.monster_type import monsters_type
from gears.armor import monster_armor
from gears.weapon import monster_attack
from gears.weapon import Weapon
from gears.armor import Armor
from bestiary.monster import Monster


class Room(Arena):

    def __init__(self,type, player) -> None:
        self.type=type
        self.player = player
        self.mob = self.GenerateMob()
        Arena.__init__(self,player,self.mob)
        winner = self.fight()
        if(winner == self.player.name):
            self.player.hp += self.player.hp * 0.2
        

    def GenerateMob(self):
        monsterType =  random.randrange(0,len(monsters_type))
        monster_name = monsters_type[monsterType]["nom"]

        weapon1 = Weapon(monster_attack[monster_name]['name'], monster_attack[monster_name]['damage'])

        armor1 = Armor(monster_armor["name"], monster_armor['defense'])

        monster =Monster(monster_name,monsters_type[monsterType]["hp"], weapon1,armor1, monsters_type[monsterType]["defense"])

        return monster
    

if __name__ == "__main__":

    test = Room.GenerateMob(Room)
    print(test)

