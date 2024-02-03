import unittest
import numpy as np
from five_in_row import (FiveInRow, PlaceState,
                            GameResult, InvalidMoveException)

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
        expected_result[0, 0] = PlaceState.WHITE
        self.assertTrue(np.array_equal(board_state, expected_result))
    
    def test_make_move_second_move(self):
        self.game.make_move(0, 0)
        self.game.make_move(1, 0)
        board_state = self.game.get_board_state()
        expected_result = np.zeros((50, 50), dtype = np.int8)
        expected_result[0, 0] = PlaceState.WHITE
        expected_result[1, 0] = PlaceState.BLACK
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
    
    def test_return_value_from_make_move_is_gameresult_inprogress(self):
        result = self.game.make_move(0, 0)
        self.assertEqual(result, GameResult.IN_PROGRESS)

    def test_get_last_move(self):
        self.game.make_move(0, 0)
        color, last_move = self.game.get_last_move()
        self.assertEqual(color, PlaceState.WHITE)
        self.assertEqual(last_move, (0, 0))
    
    def test_move_pos_from_get_last_move_is_immutable(self):
        self.game.make_move(0, 0)
        _, last_move = self.game.get_last_move()
        last_move = (1, 1)
        _, last_move = self.game.get_last_move()
        self.assertEqual(last_move, (0, 0))

if __name__ == '__main__':
    unittest.main()