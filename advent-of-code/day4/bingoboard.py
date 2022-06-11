class BingoBoard: 
    column_count = 5
    row_count = 5

    def __init__(self, numbers):
        self.board_matrix = []
        self.marked_matrix = []
        self.most_recent_number = None

        # Create matrix from list
        number_count = len(numbers)

        for lower_bound in range(0, number_count, 5):
            upper_bound = lower_bound + self.column_count
            row = []
            for n in range(lower_bound, upper_bound):
                row.append(numbers[n])
            self.board_matrix.append(row)

        # Create marked matrix
        for i in range(0, self.row_count):
            row = []
            for j in range(0, self.column_count):
                row.append(False)
            self.marked_matrix.append(row)
        
    # Looks for number on board and, if found, marks it in marked_matrix
    def mark(self, n):
        self.most_recent_number = n
        for i in range(0, self.row_count):
            for j in range(0, self.column_count):
                if self.board_matrix[i][j] == n:
                    self.marked_matrix[i][j] = True

    def is_winning_board(self):
        return self._winning_row_exists() or self._winning_column_exists()

    def _winning_row_exists(self):
        for row in range(0, self.row_count):
            winning_row_found = True
            for col in range (0, self.column_count):
                if self.marked_matrix[row][col] == False:
                    winning_row_found = False
            # winning row found
            if winning_row_found:
                return True
        # no winning rows found
        return False

    def _winning_column_exists(self):
        for col in range(0, self.column_count):
            winning_col_found = True
            for row in range(0, self.row_count):
                if self.marked_matrix[row][col] == False:
                    winning_col_found = False
            if winning_col_found:
                return True
        return False

    def calculate_score(self):
        sum = 0
        for i in range(0, self.row_count):
            for j in range(0, self.column_count):
                if self.marked_matrix[i][j] == False:
                    sum += self.board_matrix[i][j]

        return sum * self.most_recent_number

    def _print_marked(self):
        for row in self.marked_matrix:
            print(row)

    def _print_board(self):
        print(self.board_matrix)
        for row in self.board_matrix:
            print(row)