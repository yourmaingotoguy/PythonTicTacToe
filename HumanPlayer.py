from Move import Move
from Player import Player


class HumanPlayer(Player):
    """Represents the Human player and their behavior"""

    def __init__(self, board):
        super().__init__(board)

    def _get_user_input(self,prompt):
        invalid_input = True
        while invalid_input:
            print(prompt)
            user_input = input()
            if not user_input.isdigit():
                print('Input must be a number')
            else:
                user_input_int = int(user_input)
                if user_input_int < 1 or user_input_int > 3:
                    print('Input must be in the range 1-3')
                else:
                    invalid_input = False
        return user_input_int - 1

    def get_move(self):
        """Allow the human player to enter their move"""
        while True:
            row = self._get_user_input('Please enter the row: ')
            col = self._get_user_input('Please enter the column: ')
            if self.board.is_empty_cell(row,col):
                return Move(self.counter,row,col)
            else:
                print('That position is not free')
                print('Please try again')
