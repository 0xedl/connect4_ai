from Board import Board
from Player import Player
from AIPlayer import AIPlayer
import random


def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
            or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)

    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board


def process_move(player, board):
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print('\n' + str(board))

    if board.is_win_for(player.checker):
        print(player, 'wins in', player.num_moves, 'moves!')
        return True
    elif board.is_full():
        print("It's a tie!")
        return True
    else:
        return False


if __name__ == "__main__":
    connect_four(Player('X'), AIPlayer('O', 'LEFT', 3))
