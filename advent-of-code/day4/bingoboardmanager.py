from bingoboard import BingoBoard 
import re

class BingoBoardManager:
    def __init__(self, filename):
        self.number_sequence = []
        self.boards = []

        with open(filename) as f:
            self.raw_data = f.read().splitlines()
        self.get_number_sequence()
        self.get_boards()

    def get_number_sequence(self):
        first_line = self.raw_data[0]
        for n in first_line.split(","):
            self.number_sequence.append(int(n))

    def get_boards(self):
        start_row = 2
        end_row = len(self.raw_data)
        numbers = []
        for line_number in range(start_row, end_row):   
            if self.raw_data[line_number] != '':
                row = re.split('\D+', self.raw_data[line_number].strip())
                for n in row:
                    numbers.append(int(n))

            if len(numbers) == 25:
                new_board = BingoBoard(numbers)
                self.boards.append(new_board)
                numbers = []
    
    def get_winning_board_score(self):
        score = 0
        for n in self.number_sequence:
            # mark each board
            for board in self.boards:
                board.mark(n)
                # return the first board that wins
                if board.check_for_win():
                    score = board.calculate_score()
                    return score
        else:
            print("No winning boards found")