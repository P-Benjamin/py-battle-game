import random
from characters.character import Character
from room import Room
import time
import os
import pickle
class Map:

    grid = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    
    pos_player ={ 'y' : 0, 'x' : 0}
    
    boss_alive = True

    def __init__(self, player: Character, loadSave:bool):
        self.player = player
        self.loadSave = loadSave
        self.generateMap()
        self.Menu()
        self.EnterDonjon()

    def Menu(self):
        os.system('cls')
        if(not self.loadSave):
            self.Rules()
        if(self.loadSave):
            self.LoadData()
            self.Count()


    def Rules(self):
        os.system('cls')
        print("Vous allez entrer dans un donjon.")
        print("Avant de commencer, une carte de ce donjon va s'afficher puis disparaitre rapidement.")
        print("Sur cette carte :")
        print(" - P : Vous représente")
        print(" - X : Représente les salles où un monstre est présent")
        print(" - B : Représente la salle ou le Boss du donjon est situé")
        print("Votre but, tuer le Boss du donjon et libérer toutes les salles.")
        print("Attention chaque pas vous fait perdre de la vie mais vous regagnez de la vie en tuant les monstres")
        input ("Quand vous êtes prêt appuyez sur Entrée")
        self.Count()
    
    def Count(self):
        os.system('cls')
        print("Prêt ?")
        print("A la fin du décompte la carte va s'afficher")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        self.displayMap()
        time.sleep(3)
        os.system('cls')



    def EnterDonjon(self):
        while(self.boss_alive and self.player.hp>0):
            self.displayMapWithoutMark()
            print("Que voulez vous faire ?")
            print(" 1 - Allez a gauche")
            print(" 2 - Allez a droite")
            print(" 3 - Allez en haut")
            print(" 4 - Allez en bas")
            print(" 0 - Sauvegarder")
            choice=""
            while(choice not in ["0","1","2","3","4"]):
                choice = input("Vers où se déplacer : ")
            os.system('cls')
            self.Move(choice)
        if(self.player.hp <= 0):
            print("Vous avez perdu")
        if (not self.boss_alive):
            donjonClear = True
            for row in self.grid:
                if 1 in row:
                    donjonClear = False
                    break
            if (donjonClear):
                print("Bravo vous avez gagné et libéré toutes les salles")
            else:
                print("Vous avez  tuez le Boss masis vous avez oublié de libérer certaine salle")
           
        
    def Move(self,direction):
        self.player.hp -= self.player.hp * 0.1
        match int(direction):
            case 1 : self.MoveLeft()
            case 2 : self.MoveRight()
            case 3 : self.MoveUp()
            case 4 : self.MoveDown()
            case 0 : self.SaveData()
        

    def generateMap(self):
        for row in self.grid:
            number = random.randint(1,10)
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

    def displayMapWithoutMark(self):
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
                print("Il y a un monstre dans cette pièce")
                room = Room("Mob",self.player)
                room.fight()
            elif(self.grid[self.pos_player['y'] + y][self.pos_player['x'] + x] == 5):
                print("Vous entrez dans la salle du Boss")
                room = Room("Boss",self.player)
                win = room.fight()
                if(win):
                    self.boss_alive = False
            else:
                print("Il n'y a rien dans cette pièce")
            return True
        else :
            print("impossible d'aller dans cette direction")
            return False

    def SaveData(self):
        with open('map_save.pickle', 'wb') as file:
            pickle.dump(self.grid,file)
        
        with open('player_save.pickle', 'wb') as file:
            pickle.dump(self.player,file)
        
        with open('playerPos_save.pickle', 'wb') as file:
            pickle.dump(self.pos_player,file)
    
    def LoadData(self):
        with open('map_save.pickle', 'rb') as file:
            self.grid = pickle.load(file)
        
        with open('player_save.pickle', 'rb') as file:
            self.player = pickle.load(file)
        
        with open('playerPos_save.pickle', 'rb') as file:
            self.pos_player = pickle.load(file)

if __name__ == "__main__":
    generateNewMap = Map()
    print(generateNewMap.pos_player)
    generateNewMap.displayGrid()
    generateNewMap.displayMap()
    generateNewMap.MoveUp()
    generateNewMap.MoveUp()
    generateNewMap.MoveUp()
    generateNewMap.MoveUp()
    generateNewMap.MoveRight()
    generateNewMap.displayGrid()
    generateNewMap.displayMap()

