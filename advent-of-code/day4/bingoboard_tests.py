import unittest
from bingoboard import BingoBoard

class TestDay3(unittest.TestCase):
    test_numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    expected_row_count = BingoBoard.row_count
    expected_column_count = BingoBoard.column_count

    def test_marked_matrix_row_count(self):
        bingo_board = BingoBoard(self.test_numbers)

        actual_row_count = len(bingo_board.marked_matrix)
        
        self.assertTrue(actual_row_count and self.expected_row_count)

    def test_marked_matrix_col_count(self):
        bingo_board = BingoBoard(self.test_numbers)
        
        lowest_col_count = self.expected_column_count
        for row in bingo_board.marked_matrix:
            if len(row) < lowest_col_count:
                lowest_col_count = len(row)
        
        self.assertEqual(lowest_col_count, self.expected_column_count)

    def test_board_matrix_row_count(self):
        bingo_board = BingoBoard(self.test_numbers)
        
        actual_row_count = len(bingo_board.board_matrix)
        
        self.assertEqual(actual_row_count, self.expected_row_count)

    def test_board_matrix_col_count(self):
        bingo_board = BingoBoard(self.test_numbers)
        
        lowest_col_count = self.expected_column_count
        for row in bingo_board.board_matrix:
            if len(row) < lowest_col_count:
                lowest_col_count = len(row)
        
        self.assertEqual(lowest_col_count, self.expected_column_count)

    def test_board_matrix_numbers(self):
        bingo_board = BingoBoard(self.test_numbers)

        first_and_last_row_numbers_ok = True
        for row in bingo_board.board_matrix:
            if row[0] != 1 and row[self.expected_column_count-1] != 5:
                first_and_last_row_numbers_ok = False
        
        self.assertTrue(first_and_last_row_numbers_ok)

    def test_mark(self):
        bingo_board = BingoBoard(self.test_numbers)
        bingo_board.board_matrix = [
            [1, 2, 4, 5, 2], 
            [3, 2, 3, 3, 3], 
            [1, 2, 4, 2, 6], 
            [1, 3, 4, 5, 6], 
            [1, 2, 4, 5, 6]]
        number_of_twos = 6

        bingo_board.mark(2)

        mark_count = 0
        for col in range(0, self.expected_column_count):
            for row in bingo_board.marked_matrix:
                if row[col]:
                    mark_count += 1

        self.assertEqual(mark_count, number_of_twos)

    def test_winning_row_exists_true(self):
        numbers = [ 14, 21, 17, 24, 4,
                    10, 16, 15, 9, 19,
                    18, 8, 23, 26, 20,
                    22, 11, 13, 6, 5,
                    2, 0, 12, 3, 7 ]
        bingo_board = BingoBoard(numbers)

        for n in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
            bingo_board.mark(n)

        self.assertTrue(bingo_board._winning_row_exists())

    def test_winning_row_exists_false(self):
        numbers = [ 14, 21, 17, 99, 4,
                    10, 16, 15, 9, 19,
                    18, 8, 23, 26, 20,
                    22, 11, 13, 6, 5,
                    2, 0, 12, 3, 7 ]
        bingo_board = BingoBoard(numbers)

        for n in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
            bingo_board.mark(n)

        self.assertFalse(bingo_board._winning_row_exists())

    def test_winning_column_exists_true(self):
        numbers = [ 14, 3, 3, 3, 4,
                    21, 16, 15, 9, 19,
                    17, 8, 23, 26, 20,
                    24, 11, 13, 6, 5,
                    4, 0, 12, 3, 7 ]
        bingo_board = BingoBoard(numbers)

        for n in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
            bingo_board.mark(n)

        self.assertTrue(bingo_board._winning_column_exists())

    def test_winning_column_exists_false(self):
        bingo_board = BingoBoard(self.test_numbers)
        bingo_board.board_matrix = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            [4, 5, 6, 7, 8],
            [5, 6, 7, 8, 9]]

        bingo_board.mark(2)

        self.assertFalse(bingo_board._winning_column_exists())

    def test_is_winning_board_true(self):
        numbers = [ 14, 21, 17, 24, 4,
                    10, 16, 15, 9, 19,
                    18, 8, 23, 26, 20,
                    22, 11, 13, 6, 5,
                    2, 0, 12, 3, 7 ]
        bingo_board = BingoBoard(numbers)

        for n in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
            bingo_board.mark(n)

        self.assertTrue(bingo_board.is_winning_board())

    def test_is_winning_board_false(self):
        numbers = [ 1, 2, 3, 4, 5,
                    2, 3, 4, 5, 6,
                    3, 4, 5, 6, 7,
                    4, 5, 6, 7, 8,
                    5, 6, 7, 8, 9 ]
        bingo_board = BingoBoard(numbers)

        bingo_board.mark(2)
        bingo_board.mark(6)

        self.assertFalse(bingo_board.is_winning_board())

    def test_calculate_score(self):
        numbers = [ 14, 21, 17, 24, 4,
                    10, 16, 15, 9, 19,
                    18, 8, 23, 26, 20,
                    22, 11, 13, 6, 5,
                    2, 0, 12, 3, 7 ]
        bingo_board = BingoBoard(numbers)

        for n in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
            bingo_board.mark(n)
        sum = bingo_board.calculate_score()

        self.assertEqual(sum, 4512)

if __name__ == '__main__':
    unittest.main()