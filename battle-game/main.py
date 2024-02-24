from arena import Arena
from start import Start
from map import Map

start= Start()
start.Menu()
if(len(start.list_player) == 2):
    print("La bataille se lance")
    arena = Arena(start.list_player[0],start.list_player[1])
    winner = arena.fight()
    print(f"Le gagnant est {winner}")

else:
    print("Vous entrez dans un donjon")
    donjon = Map(start.list_player[0])


