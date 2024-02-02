import unittest
import numpy as np
from five_in_row import FiveInRow, InvalidMoveException

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
    
    def test_make_move_first_move(self):
        self.game.make_move(0, 0)
        board_state = self.game.get_board_state()
        expected_result = np.zeros((50, 50), dtype = np.int8)
        expected_result[0, 0] = 1
        self.assertTrue(np.array_equal(board_state, expected_result))
    
    def test_make_move_second_move(self):
        self.game.make_move(0, 0)
        self.game.make_move(1, 0)
        board_state = self.game.get_board_state()
        expected_result = np.zeros((50, 50), dtype = np.int8)
        expected_result[0, 0] = 1
        expected_result[1, 0] = -1
        self.assertTrue(np.array_equal(board_state, expected_result))
    
    def test_make_move_overlapping_second_move(self):
        self.game.make_move(0, 0)
        with self.assertRaises(InvalidMoveException) as context:
            self.game.make_move(0, 0)
        self.assertEqual(str(context.exception), "Place already taken")
    
    def test_make_move_out_of_bounds_move(self):
        with self.assertRaises(InvalidMoveException) as context:
            self.game.make_move(50, 49)
        self.assertEqual(str(context.exception), "Place out of bounds")
    
    def test_make_move_negative_coordinate(self):
        with self.assertRaises(InvalidMoveException) as context:
            self.game.make_move(-1, 0)
        self.assertEqual(str(context.exception), "Place out of bounds")

if __name__ == '__main__':
    unittest.main()