# TGFoWGame

The Fog of War game is a game akin to Battleship. Except rather than battleships there are 4 objects to be found. The four objects are:
* Circle
* Square
* Plus
* Right Triangle

The play space is divided into quadrants and can have a varying size grid. The size and position of the four objects is random.

## How to Create a Bot

To create a bot, you need to first clone the project and install the requirements, after you do this, you can use the `RandomBot.py` file as an outline for the code needed to create a bot.

The first thing you need to do is to import the two essential libraries:
```python
from FogOfWar import FogOfWar
```

You can then, create a game and print your board, each of these functions take a `player_no` parameter which expects a boolean value, you can use `True`/`False` or `1`/`0` for Player One and Player Two respectively:
```python
fOW = FogOfWar(50)
fOW.printPlayerBoard(0)
```

After this you can check the game state by calling:
```python
(board, fogBoard) = fOW.getGameState(0)
```

This will return a tuple of your board, and the fog version of the opponents board respectively.

You can attack a point on another player's board by calling `fow.attack()` which expects an x,y coordinate as the first two parameters and a player number as the third parameter. Example:
```python
fOW.attack(0, 1, 0)
```

A game will last until `fOW.isComplete()` returns true. So, when creating a bot you should create it within a while loop that checks each time.

The game ends when one player hits all the spots that contains a shape in the opponent's board.

## Note from the developer

Please don't cheat by using your opponent's board to make a decision. This will result in disqualification from the competition.
