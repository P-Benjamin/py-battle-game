from arena import Arena
from start import Start
from map import Map

class Main:
    def __init__(self) -> None:
        self.start= Start()
        self.start.menu()
        if(len(self.start.list_player) == 2):
            print("La bataille se lance")
            arena = Arena(self.start.list_player[0],self.start.list_player[1])
            winner = arena.fight()
            print(f"Le gagnant est {winner}")

        else:
            if(self.start.loadSave):
                donjon = Map(self.start.list_player[0],True)
            else:
                donjon = Map(self.start.list_player[0],False)

Main()