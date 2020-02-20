from Board import Board
from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from Counter import Counter, X, O
from random import randint


class Game:
    """ Contains the Game Playing Logic """

    def __init__(self):
        self.board = Board()
        self.human = HumanPlayer(self.board)
        self.computer = ComputerPlayer(self.board)
        self.next_player = None
        self.winner = None

    def _select_player_counter(self):
        """ Let the player select their counter """
        counter = ' '
        while not (counter == 'X' or counter == 'O'):
            print('Do you want to be X or O?')
            counter = input().upper()
            if counter != 'X' or counter != 'O':
                print('Input must be X or O')
        if counter == 'X':
            self.human.counter = X
            self.computer.counter = O
        else:
            self.human.counter = O
            self.computer.counter = X

    def _select_player_to_go_first(self):
        """ Randomly selects who will play first -"""
        if randint(0,1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer

    def play(self):
        """ Main game playing loop """
        print('Welcome to TicTacToe')
        self._select_player_counter()
        self._select_player_to_go_first()
        print(str(self.next_player) + " will go first")
        while self.winner is None:
            # Human players move
            if self.next_player == self.human:
                print(self.board)
                print('Your move')
                move = self.human.get_move()
                self.board.add_move(move)
                if self.board.check_for_winner(self.human):
                    self.winner = self.human
                else:
                    self.next_player = self.computer
            # Computer players move
            else:
                print('Computers move')
                move = self.computer.get_move()
                self.board.add_move(move)
                if self.board.check_for_winner(self.computer):
                    self.winner = self.computer
                else:
                    self.next_player = self.human

            if self.winner is not None:
                print('The winner of the game is: ' + str(self.winner))
            elif self.board.is_full():
                print('The game is a tie')
                break
        print(self.board)


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()
