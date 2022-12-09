"""
Plan:
Ideas:
write up rules
is it a linked list problem? No, I don't think so
"""

"""
Docs:

"""

import unittest
import copy

class Solution(object):


    def fuction(self, file_name, board_size):
        board = []

        for i in range(board_size):
            row = []
            for j in range(board_size):
                row.append(0)
            board.append(row)
        board_tail_visited = copy.deepcopy(board)
        board_original_state = copy.deepcopy(board)

        s_row = T_row = H_row = board_size - 1
        s_col = T_col = H_col = 0

        board[T_row][T_col] = "T"
        board[H_row][H_col] = "H"
        board_tail_visited[T_row][T_col] = 1

        with open(file_name) as f:
            for line in f:
                direction = line.split()[0]
                moves_number = int(line.split()[1])

                for move in range(moves_number):

                    if direction == "R":

                        H_col += 1

                        if H_col - T_col > 1:
                            T_col+=1

                    board = copy.deepcopy(board_original_state)

                    board[H_row][H_col] = "H"
                    board[T_row][T_col] = "T"
                    board_tail_visited[T_row][T_col] = 1
class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().fuction("09_input_test.txt", 6) == 0

    # def test_prod(self):
    #     assert Solution().fuction("09_input.txt") == 1
