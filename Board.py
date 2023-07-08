class Board:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''  # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'  # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        for col in range(self.width):
            s += ' -'
        s += '\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)

        return s

    def add_checker(self, checker, col):
        assert (checker == 'X' or checker == 'O')
        assert (0 <= col < self.width)

        for row in reversed(range(self.height)):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
        """
        checker = 'X'  # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        if col < 0 or col >= self.width:
            return False

        for row in range(self.height):
            if self.slots[row][col] == ' ':
                return True

        return False

    def is_full(self):
        for col in range(self.width):
            if self.can_add_to(col):
                return False

        return True

    def remove_checker(self, col):
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_win_for(self, checker):
        assert (checker == 'X' or checker == 'O')

        return self.is_horizontal_win(checker) or \
            self.is_vertical_win(checker) or \
            self.is_down_diagonal_win(checker) or \
            self.is_up_diagonal_win(checker)

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                        self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                        self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                # Check if the next four rows in this column
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                        self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False

    def is_down_diagonal_win(self, checker):
        """Checks for a down diagonal win for the specified checker."""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                        self.slots[row + 3][col + 3] == checker:
                    return True

        return False

    def is_up_diagonal_win(self, checker):
        """Checks for an up diagonal win for the specified checker."""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                        self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                        self.slots[row - 3][col + 3] == checker:
                    return True

        return False

    def reset(self):
        self.slots = [[' '] * self.width for row in range(self.height)]
