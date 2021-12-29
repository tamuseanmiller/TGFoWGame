from FogOfWar import FogOfWar
from Board import PointState
import random

fOW = FogOfWar(50)
(b, fB) = fOW.getGameState(False)
for i in range(0, 50):
    for j in range(0, 50):
        if b[i][j] == PointState.SQUARE:
            print('S', "  ", end='')
        elif b[i][j] == PointState.CIRCLE:
            print('C', "  ", end='')
        elif b[i][j] == PointState.PLUS:
            print('P', "  ", end='')
        elif b[i][j] == PointState.TRIANGLE:
            print('T', "  ", end='')
        else:
            print('-', "  ", end='')
    print("\n")

# print("\n")
# for i in range(0, 50):
#     for j in range(0, 50):
#         fOW.attack(i, j, False)

possMovesA = set()
possMovesB = set()

for i in range(0, 50):
    for j in range(0, 50):
        possMovesA.add((i, j))
        possMovesB.add((i, j))

while not fOW.isComplete():
    randPointA = random.sample(possMovesA, 1)
    randPointB = random.sample(possMovesB, 1)
    fOW.attack(randPointA[0][0], randPointA[0][1], True)
    fOW.attack(randPointB[0][0], randPointB[0][1], False)
    possMovesA.remove(randPointA[0])
    possMovesB.remove(randPointB[0])

(b, fB) = fOW.getGameState(False)

# print("\n")
# for i in range(0, 50):
#     for j in range(0, 50):
#         if fB[i][j] == PointState.UNKNOWN:
#             print('U', "  ", end='')
#         if fB[i][j] == PointState.HIT:
#             print('H', "  ", end='')
#         if fB[i][j] == PointState.MISS:
#             print('M', "  ", end='')
#     print("\n")
