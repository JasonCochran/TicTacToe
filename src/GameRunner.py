from Game import *


if __name__ == '__main__':
    keep_playing = True

    print 'Welcome to the best game of Tic Tac Toe'
    print 'Please select what symbol you would like to play as'
    symbol = raw_input()

    while symbol.__len__() != 1:
        print 'Please input a symbol of length 1'
        symbol = raw_input()

    game = Game(symbol)

    while True:
        while game.game_in_progress:
            print 'Make your move by typing the location of where you want go next'
            game.print_board()
            move = raw_input()
            while game.player_move(move):
                print "Invalid move. Please select a valid location"
                move = raw_input()

        print game.game_outcome_string

        print 'Would you like to keep playing? Enter [y/n]'
        player_input = raw_input()
        if player_input == 'n':
            break
        elif player_input != 'y':
            print 'Invalid input. Now you have to play again :)'
