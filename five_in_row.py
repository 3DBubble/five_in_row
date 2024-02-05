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

    @staticmethod
    def get_win(color : PlaceState):
        return GameResult.WHITE_WIN if color == PlaceState.WHITE else GameResult.BLACK_WIN

class InvalidMoveException(Exception):
    pass

class FiveInRow:
    def __init__(self, board_shape = (50, 50)) -> None:
        self.__board = np.zeros(board_shape, dtype = np.int8)
        self.__next_move = PlaceState.WHITE
        self.__last_move_pos = None
    
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
    
    def __check_win_line_correlation(self, line, ones, col) -> GameResult:
        return GameResult.get_win(col) if (np.correlate(line, ones, mode='valid') == 5 * col).any() else GameResult.IN_PROGRESS
    
    def check_win(self) -> GameResult:
        '''Check if there is win'''

        if self.__last_move_pos is None:
            return GameResult.IN_PROGRESS
        
        x, y = self.__last_move_pos
        col = PlaceState.toggle_move(self.__next_move).value
        ones = np.ones(5, dtype = np.int8)

        # check horizontal line
        line_h = self.__board[x, :]
        result = self.__check_win_line_correlation(line_h, ones, col)
        if result != GameResult.IN_PROGRESS:
            return result
        
        # check vertical line
        line_v = self.__board[:, y]
        result = self.__check_win_line_correlation(line_v, ones, col)
        if result != GameResult.IN_PROGRESS:
            return result
        
        # check diagonal line
        line_d1 = np.diag(self.__board, y - x)
        result = self.__check_win_line_correlation(line_d1, ones, col)
        if result != GameResult.IN_PROGRESS:
            return result
        
        # check second-diagonal line
        line_d2 = np.diag(np.flipud(self.__board), 1 - self.__board.shape[0] + x + y)
        result = self.__check_win_line_correlation(line_d2, ones, col)
        if result != GameResult.IN_PROGRESS:
            return result
        
        return GameResult.IN_PROGRESS
    
    def make_move(self, move_pos_x, move_pos_y):
        self.check_valid_move(move_pos_x, move_pos_y)

        self.__board[move_pos_x, move_pos_y] = self.__next_move.value
        self.__last_move_pos = (move_pos_x, move_pos_y)
        self.__next_move = PlaceState.toggle_move(self.__next_move)
        return self.check_win()

    def get_last_move(self):
        return PlaceState.toggle_move(self.__next_move), self.__last_move_pos