class Board:
    def __init__(self):
        self.board = []
        self.x_size = 3
        self.y_size = 3
        self.initialize_board()

    def initialize_board(self):
        k = 1
        for i in range(self.x_size):
            self.board.append([])
            for j in range(self.y_size):
                self.board[i].append(k)
                k = + 1

    def get_location(self, x, y):
        return self.board[x][y]

    def validate_move(self, location):
        x, y = self.__convert_location(location)
        if self.board[x][y] == '[ ]':
            return True
        else:
            return False

    def make_move(self, location, symbol):
        x, y = self.__convert_location(location)
        self.board[x][y] = symbol

    def is_occupied(self, x, y):
        if self.board[x][y] != '[ ]':
            return True
        else:
            return False

    def __convert_location(self, location):
        x = location % 3
        y = location / 3
        return x, y
