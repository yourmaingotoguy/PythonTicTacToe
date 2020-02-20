from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    """Abstract class representing a Player and their counter"""

    def __init__(self, board):
        self.board = board
        self._counter = None

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self,value):
        self._counter = value

    @abstractmethod
    def get_move(self):
        pass

    def __str__(self):
        return self.__class__.__name__ + '[' + str(self.counter) + ']'
