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

        T_row = H_row = T_col = H_col = board_size // 2

        board[T_row][T_col] = "T"
        board[H_row][H_col] = "H"
        board_tail_visited[T_row][T_col] = 1

        line_number = 0
        with open(file_name) as f:
            for line in f:
                line_number+=1
                try:
                    direction = line.split()[0]
                    moves_number = int(line.split()[1])

                    if direction == "R":

                        for move in range(moves_number):

                            H_col += 1

                            if H_col - T_col > 1:
                                T_col+=1

                                if H_row - T_row > 0:
                                    T_row+=1
                                elif H_row - T_row < 0:
                                    T_row -= 1
                            # board = copy.deepcopy(board_original_state)

                            board[H_row][H_col] = "H"
                            board[T_row][T_col] = "T"
                            board_tail_visited[T_row][T_col] = 1

                    elif direction == "U":
                        for move in range(moves_number):

                            H_row -= 1

                            if H_row - T_row <- 1:
                                T_row-=1

                                if H_col - T_col > 0:
                                    T_col+=1

                                elif H_col - T_col < 0:
                                    T_col-=1

                            # board = copy.deepcopy(board_original_state)

                            board[H_row][H_col] = "H"
                            board[T_row][T_col] = "T"
                            board_tail_visited[T_row][T_col] = 1

                    elif direction == "L":
                        for move in range(moves_number):

                            H_col -= 1

                            if H_col - T_col < -1:
                                T_col-=1

                                if H_row - T_row > 0:
                                    T_row += 1
                                elif H_row - T_row < 0:
                                    T_row -= 1

                            # board = copy.deepcopy(board_original_state)

                            board[H_row][H_col] = "H"
                            board[T_row][T_col] = "T"
                            board_tail_visited[T_row][T_col] = 1

                    elif direction == "D":
                        for move in range(moves_number):

                            H_row += 1

                            if H_row - T_row > 1:
                                T_row+=1

                                if H_col - T_col > 0:
                                    T_col+=1

                                elif H_col - T_col < 0:
                                    T_col-=1

                            # board = copy.deepcopy(board_original_state)

                            board[H_row][H_col] = "H"
                            board[T_row][T_col] = "T"
                            board_tail_visited[T_row][T_col] = 1



                except Exception as e:
                    print(e)
                    print(line_number, line)
            result = 0
            for row in board_tail_visited:
                result += sum(row)
            return result

class TestCase(unittest.TestCase):

    def test_dev(self):
        self.assertEqual(13, Solution().fuction("09_input_test.txt", 12))

    def test_prod(self):
        self.assertEqual(6181,  Solution().fuction("09_input.txt", 1000))
