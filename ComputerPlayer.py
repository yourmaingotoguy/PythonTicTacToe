from Move import Move
from Player import Player
from random import randint


class ComputerPlayer(Player):
    def __init__(self,board):
        super().__init__(board)

    def randomly_select_cell(self):
        """Use a simplistic random selection approach to find a cell to fill """
        while True:
            #Randomly select a cell
            row = randint(0,2)
            col = randint(0,2)
            # Check to see if the cel is empty
            if self.board.is_empty_cell(row,col):
                return Move(self.counter,row,col)

    def get_move(self):
        """ Provide a very simple algorithm for selecting a move """
        if self.board.is_empty_cell(1,1):
            return Move(self.counter,1,1)
        elif self.board.is_empty_cell(0,0):
            return Move(self.counter,0,0)
        elif self.board.is_empty_cell(2,2):
            return Move(self.counter, 2, 2)
        elif self.board.is_empty_cell(0, 2):
            return Move(self.counter,0,2)
        elif self.board.is_empty_cell(2, 0):
            return Move(self.counter,2,0)
        else:
            return self.randomly_select_cell()