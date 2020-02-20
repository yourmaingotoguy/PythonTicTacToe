class Board:
    """the tic tac toe board"""

    def __init__(self):
        # Set up the 3 by 3 of cells
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.separator = '\n' + ('-' * 11) + '\n'

    def __str__(self):
        row1 = ' ' + str(self.cells[0][0]) + ' | ' + str(self.cells[0][1]) + ' | ' + str(self.cells[0][2])
        row2 = ' ' + str(self.cells[1][0]) + ' | ' + str(self.cells[1][1]) + ' | ' + str(self.cells[1][2])
        row3 = ' ' + str(self.cells[2][0]) + ' | ' + str(self.cells[2][1]) + ' | ' + str(self.cells[2][2])
        return row1 + self.separator + row2 + self.separator + row3

    def add_move(self,move):
        """Add a move to the board'"""
        row = self.cells[move.x]
        row[move.y] = move.counter

    def is_empty_cell(self,row,col):
        return self.cells[row][col] == ' '

    def cell_contains(self,counter,row,col):
        """ Check to see if a cell contains the provided counter"""
        return self.cells[row][col] == counter

    def is_full(self):
        """Check to see if the board is full or not"""
        for row in range(0,3):
            for col in range(0,3):
                if self.is_empty_cell(row,col):
                    return False
        return True

    def check_for_winner(self,player):
        c = player.counter
        return (
            # across the top
            (self.cell_contains(c, 0, 0) and self.cell_contains(c, 0, 1) and self.cell_contains(c, 0, 2)) or
            # across the middle
            (self.cell_contains(c, 1, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 1, 2)) or
            # across the bottom
            (self.cell_contains(c, 2, 0) and self.cell_contains(c, 2, 1) and self.cell_contains(c, 2, 2)) or
            # down the left side
            (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 0) and self.cell_contains(c, 2, 0)) or
            # down the middle
            (self.cell_contains(c, 0, 1) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 1)) or
            # across the right side
            (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 2) and self.cell_contains(c, 2, 2)) or
            # diagonal
            (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 2)) or
            # other diagonal
            (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 0))
        )