from FogOfWar import FogOfWar
import random

fOW = FogOfWar(50)
(b, fB) = fOW.getGameState(False)
fOW.printPlayerBoard(0)

# Create possible moves and add them
possMovesA = set()
possMovesB = set()
for i in range(0, fOW.size):
    for j in range(0, fOW.size):
        possMovesA.add((i, j))
        possMovesB.add((i, j))

# Run random points in the sets until the game ends
while not fOW.isComplete():
    randPointA = random.sample(possMovesA, 1)
    randPointB = random.sample(possMovesB, 1)
    fOW.attack(randPointA[0][0], randPointA[0][1], True)
    fOW.attack(randPointB[0][0], randPointB[0][1], False)
    possMovesA.remove(randPointA[0])
    possMovesB.remove(randPointB[0])

(b, fB) = fOW.getGameState(False)
