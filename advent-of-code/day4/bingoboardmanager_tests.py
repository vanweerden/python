import unittest
from bingoboardmanager import BingoBoardManager

class TestDay3(unittest.TestCase):
    filename = 'test_input.txt'

    def test_get_number_sequence(self):
        bb_manager = BingoBoardManager(self.filename)
            
        expected = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        self.assertListEqual(bb_manager.number_sequence, expected)

    def test_get_boards_first_board(self):
        bb_manager = BingoBoardManager(self.filename)
        actual = bb_manager.boards[0].board_matrix
        
        expected = [[22,13,17,11,0], [8,2,23,4,24], [21,9,14,16,7], [6,10,3,18,5], [1,12,20,15,19]]
        self.assertListEqual(actual, expected)

    def test_get_boards_count(self):
        bb_manager = BingoBoardManager(self.filename)

        actual = len(bb_manager.boards)
        expected = 3

        self.assertEqual(actual, expected)


    def test_first_winning_board_score(self):
        bb_manager = BingoBoardManager(self.filename)
        bb_manager.get_board_scores()

        actual = bb_manager.first_winning_board_score()
        expected = 4512

        self.assertEqual(actual, expected)

    def test_last_winning_board(self):
        bb_manager = BingoBoardManager(self.filename)
        bb_manager.get_board_scores()

        actual = bb_manager.last_winning_board_score()
        expected = 1924

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()