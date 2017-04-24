from Board import *
from Game import *


class AI:
    def __init__(self, board):
        self.__board = board

    def make_move(self, board):
        self.__board = board # Update to the newest game state
        self.__get_move()
        return self.__board

    def __get_move(self):
        if not self.__board.is_occupied(2, 2): # Awlways prefer to start in the center
            self.__board.make_move(2, 2)


