from arena import Arena
from start import Start

start= Start()
arena = Arena(start.list_player[0],start.list_player[1])
winner = arena.fight()

print(winner)
