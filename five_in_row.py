import numpy as np
from enum import IntEnum

class PlaceState(IntEnum):
    WHITE = 1,
    BLACK = -1,
    EMPTY = 0

    @staticmethod
    def toggle_move(move):
        if move == PlaceState.WHITE:
            return PlaceState.BLACK
        elif move == PlaceState.BLACK:
            return PlaceState.WHITE
        else:
            return PlaceState.EMPTY

class FiveInRow:
    def __init__(self, board_shape = (50, 50)) -> None:
        self.__board = np.zeros(board_shape, dtype = np.int8)
        self.__next_move = PlaceState.WHITE
    
    def get_board_state(self):
        return self.__board.copy()
    
    def make_move(self, move_pos_x, move_pos_y):
        self.__board[move_pos_x, move_pos_y] = self.__next_move.value
        self.__next_move = PlaceState.toggle_move(self.__next_move)
