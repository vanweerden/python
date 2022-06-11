from bingoboardmanager import BingoBoardManager

input = 'input.txt'
board_manager = BingoBoardManager(input)
board_manager.get_board_scores()

print("Part 1: Score of first winning board:")
print(board_manager.first_winning_board_score())
print("Part 2: Score of last winning board:")
print(board_manager.last_winning_board_score())
