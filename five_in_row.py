import numpy as np

class FiveInRow:
    def __init__(self, board_shape = (50, 50)) -> None:
        self.__board = np.zeros(board_shape, dtype = np.int8)
    
    def get_board_state(self):
        return self.__board.copy()