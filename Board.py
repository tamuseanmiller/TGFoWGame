import enum
import random
import math


class PointState(enum.Enum):
    UNKNOWN = 0
    HIT = 1
    MISS = 2
    CIRCLE = 3
    SQUARE = 4
    PLUS = 5
    TRIANGLE = 6


class Board:

    def __init__(self, size=100) -> None:
        self.board_size = size
        self.grid = [[PointState.UNKNOWN for x in range(size)] for y in range(size)]
        self.grid_fog = [[PointState.UNKNOWN for x in range(size)] for y in range(size)]
        self.numLeft = 0

    def getBoardState(self):
        return self.grid

    def updateHitOrMiss(self, x: int, y: int) -> bool:
        # If it's a hit
        if self.grid[x][y] == PointState.SQUARE or self.grid[x][y] == PointState.PLUS or \
                self.grid[x][y] == PointState.CIRCLE or self.grid[x][y] == PointState.TRIANGLE:
            self.grid[x][y] = PointState.HIT
            self.grid_fog[x][y] = PointState.HIT
            self.numLeft -= 1
            return True
        else:
            self.grid[x][y] = PointState.MISS
            self.grid_fog[x][y] = PointState.MISS
            return False
        # elif self.grid == PointState.PLUS:
        #     self.grid[x][y] = PointState.HIT
        # elif self.grid == PointState.CIRCLE:
        #     self.grid[x][y] = PointState.HIT
        # elif self.grid == PointState.TRIANGLE:
        #     self.grid[x][y] = PointState.HIT

    # Randomizes the board, returns an integer of the number of points where a shape exists
    def randomizeBoard(self):
        available_shapes = [PointState.CIRCLE, PointState.SQUARE, PointState.PLUS,
                            PointState.TRIANGLE]
        available_areas = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for i in range(4):
            current_shape = random.randint(0, len(available_shapes) - 1)
            current_area = random.randint(0, len(available_areas) - 1)
            area_x = int(available_areas[current_area][0] * self.board_size / 2)
            area_y = int(available_areas[current_area][1] * self.board_size / 2)

            # If Square
            if available_shapes[current_shape] == PointState.SQUARE:
                side_length = random.randint(2, int(self.board_size / 2) - 1)
                for x in range(area_x, side_length + area_x):
                    for y in range(area_y, side_length + area_y):
                        self.grid[x][y] = PointState.SQUARE
                        self.numLeft += 1

            # If Triangle
            elif available_shapes[current_shape] == PointState.TRIANGLE:
                side_length = random.randint(int(self.board_size / 10), int(self.board_size / 2) - 1)
                for x in range(area_x, area_x + side_length):
                    for y in range(area_y, area_y + x + 1 - area_x):
                        self.grid[x][y] = PointState.TRIANGLE
                        self.numLeft += 1

            # If Plus
            elif available_shapes[current_shape] == PointState.PLUS:
                length_of_rec = random.randint(2, int(self.board_size / 2) - 1)
                width_of_rec = int(length_of_rec / 3)

                # Draw Rectangle 1
                for x in range(area_x, area_x + length_of_rec):
                    for y in range(area_y + width_of_rec, area_y + width_of_rec * 2):
                        self.grid[x][y] = PointState.PLUS
                        self.numLeft += 1

                # Draw Rectangle 2
                for x in range(area_x + width_of_rec, area_x + width_of_rec * 2):
                    for y in range(area_y, area_y + length_of_rec):
                        self.grid[x][y] = PointState.PLUS
                        if self.grid[x][y] != PointState.PLUS:
                            self.numLeft += 1

            # IF Circle
            elif available_shapes[current_shape] == PointState.CIRCLE:
                radius = random.randint(2, math.floor((self.board_size / 2 - 1) / 2))
                for x in range(area_x, radius * 2 + area_x):
                    for y in range(area_y, radius * 2 + area_y):
                        p1 = [area_x + radius, area_y + radius]
                        p2 = [x, y]
                        if math.dist(p1, p2) <= radius:
                            self.grid[x][y] = PointState.CIRCLE
                            self.numLeft += 1

            # Remove used shapes/areas
            available_shapes.remove(available_shapes[current_shape])
            available_areas.remove(available_areas[current_area])
