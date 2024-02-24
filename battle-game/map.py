import random
from characters.character import Character
from room import Room
class Map:

    grid = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    
    pos_player ={ 'y' : 0, 'x' : 0}
    
    boss_alive = True

    def __init__(self, player: Character):
        self.player = player
        self.generateMap()
        self.EnterDonjon()


    def EnterDonjon(self):
        while(self.boss_alive and self.player.hp>0):
            print("Que voulez vous faire ?")
            print(" 1 - Allez a gauche")
            print(" 2 - Allez a droite")
            print(" 3 - Allez en haut")
            print(" 4 - Allez en bas")
            choice = input()
            self.Move(choice)
            self.displayMap()
        if(self.player.hp <= 0):
            print("Vous avez perdu")
        
    def Move(self,direction):
        match int(direction):
            case 1 : self.MoveLeft()
            case 2 : self.MoveRight()
            case 3 : self.MoveUp()
            case 4 : self.MoveDown()
        

    def generateMap(self):
        for row in self.grid:
            number = random.randint(1,3)
            for i in range(0,number):
                monster = random.randint(0,9)
                row[monster] = 1

        start = random.randint(0,5)
        while self.grid[start][0] == 1:
            start = random.randint(0,5)
        self.grid[start][0] = 9
        

        end = random.randint(0,5)
        while self.grid[end][9] == 1:
            end = random.randint(0,5)
        self.grid[end][9] = 5
        self.pos_player['y'] = start

    def displayGrid(self):
        for row in self.grid:
            for r in row:
                print(r, end="")    
            print()

    def displayMap(self):
        side = "|---|---|---|---|---|---|---|---|---|---|"
        middle = "|   |   |   |   |   |   |   |   |   |   |"
        newmiddle =""

        print(side)
        for row in self.grid:
            newmiddle = middle
            i = -2

            for index,r in enumerate(row):
                i += 4
                if (r == 9):
                    newmiddle = newmiddle[:i] + "P" + newmiddle[i +1:]
                if (r == 1 ):
                    newmiddle = newmiddle[:i] + "X" + newmiddle[i+1:]
                if (r == 5 and index > 0):
                    newmiddle = newmiddle[:i] + "B" + newmiddle[i +1:]


            print(newmiddle)
            print(side)

    def MoveUp(self):
        if(self.CheckNewPos(0,-1)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y'] -1 ][self.pos_player['x']] = 9
            self.pos_player['y'] -= 1 
    
    def MoveDown(self):
        if(self.CheckNewPos(0,1)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y'] +1 ][self.pos_player['x']] = 9
            self.pos_player['y'] += 1 


    def MoveRight(self):
        if(self.CheckNewPos(1,0)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y']][self.pos_player['x'] + 1] = 9
            self.pos_player['x'] += 1 


    def MoveLeft(self):
        if(self.CheckNewPos(-1,0)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y']][self.pos_player['x'] - 1] = 9
            self.pos_player['x'] -= 1 


    def CheckNewPos(self, x:int, y:int):
        if(self.pos_player['y'] + y <= 5 and self.pos_player['y'] + y >= 0 and self.pos_player['x'] + x <= 9 and self.pos_player['x'] + x >= 0 ):
            if(self.grid[self.pos_player['y'] + y][self.pos_player['x'] + x] == 1):
                print("Mob in this room")
                room = Room("mob",self.player)
            elif(self.grid[self.pos_player['y'] + y][self.pos_player['x'] + x] == 5):
                print("Boss in this room")
                self.boss_alive = False
            else:
                print("Nothing in this room")
            return True
        else :
            print("impossible d'aller dans cette direction")
            return False



if __name__ == "__main__":
    generateNewMap = Map()
    print(generateNewMap.pos_player)
    generateNewMap.displayGrid()
    generateNewMap.deisplayMap()
    generateNewMap.MoveUp()
    generateNewMap.MoveUp()
    generateNewMap.MoveUp()
    generateNewMap.MoveUp()
    generateNewMap.MoveRight()
    generateNewMap.displayGrid()
    generateNewMap.deisplayMap()

