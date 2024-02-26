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
        self.generate_map()
        self.menu()
        self.enter_donjon()

    def menu(self):
        os.system('cls')
        if(not self.loadSave):
            self.rules()
        if(self.loadSave):
            self.load_data()
            self.count()


    def rules(self):
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
        self.count()
    
    def count(self):
        os.system('cls')
        print("Prêt ?")
        print("A la fin du décompte la carte va s'afficher")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        self.display_map()
        time.sleep(3)
        os.system('cls')



    def enter_donjon(self):
        while(self.boss_alive and self.player.hp>0):
            self.display_map_without_mark()
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
            self.move(choice)
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
           
        
    def move(self,direction):
        self.player.hp -= self.player.hp * 0.1
        match int(direction):
            case 1 : self.move_left()
            case 2 : self.move_right()
            case 3 : self.move_up()
            case 4 : self.move_down()
            case 0 : self.save_data()
        

    def generate_map(self):
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

    def display_grid(self):
        for row in self.grid:
            for r in row:
                print(r, end="")    
            print()

    def display_map(self):
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

    def display_map_without_mark(self):
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

    def move_up(self):
        if(self.check_new_pos(0,-1)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y'] -1 ][self.pos_player['x']] = 9
            self.pos_player['y'] -= 1 
    
    def move_down(self):
        if(self.check_new_pos(0,1)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y'] +1 ][self.pos_player['x']] = 9
            self.pos_player['y'] += 1 


    def move_right(self):
        if(self.check_new_pos(1,0)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y']][self.pos_player['x'] + 1] = 9
            self.pos_player['x'] += 1 


    def move_left(self):
        if(self.check_new_pos(-1,0)):
            self.grid[self.pos_player['y']][self.pos_player['x']] = 0
            self.grid[self.pos_player['y']][self.pos_player['x'] - 1] = 9
            self.pos_player['x'] -= 1 


    def check_new_pos(self, x:int, y:int):
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

    def save_data(self):
        with open('save/map_save.pickle', 'wb') as file:
            pickle.dump(self.grid,file)
        
        with open('save/player_save.pickle', 'wb') as file:
            pickle.dump(self.player,file)
        
        with open('save/playerPos_save.pickle', 'wb') as file:
            pickle.dump(self.pos_player,file)
    
    def load_data(self):
        with open('save/map_save.pickle', 'rb') as file:
            self.grid = pickle.load(file)
        
        with open('save/player_save.pickle', 'rb') as file:
            self.player = pickle.load(file)
        
        with open('save/playerPos_save.pickle', 'rb') as file:
            self.pos_player = pickle.load(file)

if __name__ == "__main__":
    generateNewMap = Map()
    print(generateNewMap.pos_player)
    generateNewMap.display_grid()
    generateNewMap.display_map()
    generateNewMap.move_up()
    generateNewMap.move_up()
    generateNewMap.move_up()
    generateNewMap.move_up()
    generateNewMap.move_right()
    generateNewMap.display_grid()
    generateNewMap.display_map()

