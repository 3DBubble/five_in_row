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

class GameResult(IntEnum):
    IN_PROGRESS = 0,
    WHITE_WIN = 1,
    BLACK_WIN = 2,
    DRAW = 3

class InvalidMoveException(Exception):
    pass

class FiveInRow:
    def __init__(self, board_shape = (50, 50)) -> None:
        self.__board = np.zeros(board_shape, dtype = np.int8)
        self.__next_move = PlaceState.WHITE
    
    def get_board_state(self):
        return self.__board.copy()
    
    def check_valid_move(self, move_pos_x, move_pos_y):
        '''Check if the move is valid
        raises InvalidMoveException if the move is invalid'''

        if move_pos_x < 0 or move_pos_x >= self.__board.shape[0] \
            or move_pos_y < 0 or move_pos_y >= self.__board.shape[1]:
            raise InvalidMoveException("Place out of bounds")

        if self.__board[move_pos_x, move_pos_y] != PlaceState.EMPTY:
            raise InvalidMoveException("Place already taken")
    
    def make_move(self, move_pos_x, move_pos_y):
        self.check_valid_move(move_pos_x, move_pos_y)

        self.__board[move_pos_x, move_pos_y] = self.__next_move.value
        self.__last_move_pos = (move_pos_x, move_pos_y)
        self.__next_move = PlaceState.toggle_move(self.__next_move)

        return GameResult.IN_PROGRESS

    def get_last_move(self):
        return PlaceState.toggle_move(self.__next_move), self.__last_move_pos