from Board import Board
import coloredlogs, logging


class FogOfWar:

    def __init__(self, size: int):
        # Create un-fogged boards
        self.player_one_board = Board(size)
        self.player_one_board.randomizeBoard()
        self.player_two_board = Board(size)
        self.player_two_board.randomizeBoard()

        # Create fog boards
        self.player_one_fog = self.player_two_board.grid_fog
        self.player_two_fog = self.player_one_board.grid_fog

        # Create a logger object.
        self.logger = logging.getLogger(__name__)

        # Don't want to see log messages from libraries
        coloredlogs.install(level='DEBUG', logger=self.logger)

        # Constructor information
        self.logger.info("Welcome to the Turing Games Fog Of War Game!")

    # Takes an x, y, and player number and updates the hits on the board
    def attack(self, x: int, y: int, player_no: bool):
        if not player_no:
            if self.player_one_board.updateHitOrMiss(x, y):
                self.logger.critical(f'Player Two has hit Player One\'s Board at point ({x}, {y})')
            else:
                self.logger.warning(f'Player Two has missed Player One\'s Board at point ({x}, {y})')

        else:
            if self.player_two_board.updateHitOrMiss(x, y):
                self.logger.critical(f'Player One has hit Player Two\'s Board at point ({x}, {y})')
            else:
                self.logger.warning(f'Player One has missed Player Two\'s Board at point ({x}, {y})')

    # Returns your board and then the fog board of the other player respectively as a tuple
    def getGameState(self, player_no: bool) -> tuple:
        if player_no:
            return self.player_one_board.grid, self.player_one_fog
        else:
            return self.player_two_board.grid, self.player_two_fog

    def isComplete(self):
        if self.player_one_board.numLeft == 0:
            self.logger.info("Player One has won the game!")
        elif self.player_two_board.numLeft == 0:
            self.logger.info("Player Two has won the game!")
        return self.player_one_board.numLeft == 0 or self.player_two_board.numLeft == 0

