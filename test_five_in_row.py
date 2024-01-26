import unittest
import numpy as np
from five_in_row import FiveInRow

class TestFiveInRow(unittest.TestCase):
    def setUp(self) -> None:
        self.game = FiveInRow()
    
    def test_get_board_state(self):
        board_state = self.game.get_board_state()
        expected_result = np.zeros((50, 50), dtype = np.int8)
        self.assertTrue(np.array_equal(board_state, expected_result))

    def test_get_board_state_with_custom_shape(self):
        game1 = FiveInRow(board_shape = (20, 20))
        board_state = game1.get_board_state()
        expected_result = np.zeros((20, 20), dtype = np.int8)
        self.assertTrue(np.array_equal(board_state, expected_result))

if __name__ == '__main__':
    unittest.main()