
class Player:
    def __init__(self, checker):
        assert (checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        return "Player " + self.checker

    def opponent_check(self):
        if self.checker == 'O':
            return 'X'
        return 'O'

    def next_move(self, board):
        col_str = input("Enter a column: ")
        try:
            col = int(col_str)
            if board.can_add_to(col):
                self.num_moves += 1
                return col
            else:
                print("Invalid column number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid column number.")
