from Board import *


class Game:
    def __init__(self, player_symbol):
        self.board = Board()
        self.player_score = 0
        self.ai_score = 0
        self.player_symbol = player_symbol
        if player_symbol == 'X':
            self.ai_symbol = 'O'
        else:
            self.ai_symbol = 'X'
        self.game_outcome_string = 'Game in progress'
        self.game_in_progress = True

    def player_move(self, location):
        if self.board.validate_move(location):
            return True
        else:
            return False

    def print_board(self):
        for i in range(1, self.board.x_size ):
            for j in range(1, self.board.y_size ):
                if i == 1 and j == 1:
                    print "    1  2  3 "
                    print "------------"
                if i == 1:
                    print str(j) + " |"

                print self.board.get_location(i, j)
