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


class Solution(object):
    def fuction(self, file_name, board_size):
        board = []
        indexes = []
        for i in range(board_size):
            row = []
            visited_row = []
            for j in range(board_size):
                row.append(j)
                visited_row.append(0)
            indexes.append(row)
            board.append(visited_row)

        s_row = T_row = H_row = board_size - 1
        s_col = T_col = H_col = 0

        board[s_row][s_col] = "H"

        with open(file_name) as f:
            for line in f:
                direction = line.split()[0]
                moves_number = int(line.split()[1])

                board[H_row][H_col] = "H"
                board[T_row][T_col] = "T"

                board[H_row][H_col] = 1

                if direction == "R":
                    for move in range(moves_number):

                        H_col += 1

                        if H_col - T_col >=1:
                            T_col+=1

        result = 0

        return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().fuction("09_input_test.txt", 6) == 0

    # def test_prod(self):
    #     assert Solution().fuction("09_input.txt") == 1
