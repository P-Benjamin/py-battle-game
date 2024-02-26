from arena import Arena
from start import Start
from map import Map

start= Start()
start.menu()
if(len(start.list_player) == 2):
    print("La bataille se lance")
    arena = Arena(start.list_player[0],start.list_player[1])
    winner = arena.fight()
    print(f"Le gagnant est {winner}")

else:
    if(start.loadSave):
        donjon = Map(start.list_player[0],True)
    else:
        donjon = Map(start.list_player[0],False)



