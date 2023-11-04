from bingoboard import BingoBoard 
import re

class BingoBoardManager:
    def __init__(self, filename):
        self.number_sequence = []
        self.boards = []
        self.win_order = []
        self.scores = []

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
    
    def get_board_scores(self):
        board_count = len(self.boards)
        self.scores = [0]*board_count
        self.win_order = [0]*board_count
        done = [False]*board_count
        win_counter = 1

        for n in self.number_sequence:
            for index, board in zip(range(board_count), self.boards):
                board.mark(n)
                if not done[index] and board.is_winning_board():
                    score = board.calculate_score()
                    self.scores[index] = score
                    self.win_order[index] = win_counter
                    win_counter += 1
                    done[index] = True

    def first_winning_board_score(self):
        board_count = len(self.boards)

        for index, position in zip(range(board_count), self.win_order):
            if position == 1:
                return self.scores[index]

    def last_winning_board_score(self):
        # return last non-zero score 
        last_position = len(self.boards)+1

        # iterate backwards starting with board count
        for position in reversed(range(1, last_position)):
            # find index of item in win_order that equals current index
            index = self.win_order.index(position)
            if self.scores[index] > 0:
                return self.scores[index]