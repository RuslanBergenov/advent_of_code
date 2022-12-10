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

        s = board_size // 2

        H_row = H_col = _1_row = _1_col = _2_row = _2_col = _3_row = _3_col = _4_row = _4_col = _5_row = _5_col = _6_row = _6_col = _7_row = _7_col = _8_row = _8_col = _9_row = _9_col = s

        board[H_row][H_col] = "H"
        board_tail_visited[_9_row][_9_col] = 1

        coordinates = {
            "H": {"row": s, "col": s},
            "1": {"row": s, "col": s},
            "2": {"row": s, "col": s},
            "3": {"row": s, "col": s},
            "4": {"row": s, "col": s},
            "5": {"row": s, "col": s},
            "6": {"row": s, "col": s},
            "7": {"row": s, "col": s},
            "8": {"row": s, "col": s},
            "9": {"row": s, "col": s}}


        def calculate_tail_coordinates_while_moving_right(head_row, head_column, tail_row, tail_column):

            if head_column - tail_column > 1:
                tail_column += 1

                if head_row - tail_row > 0:
                    tail_row += 1
                elif head_row - tail_row < 0:
                    tail_row -= 1
            return tail_row, tail_column

        line_number = 0
        with open(file_name) as f:
            for line in f:
                line_number += 1
                try:
                    direction = line.split()[0]
                    moves_number = int(line.split()[1])

                    if direction == "R":

                        for move in range(moves_number):

                            H_col += 1

                            for index, row_and_col in enumerate(coordinates[1:]):
                                row_and_col[0], row_and_col[1] = calculate_tail_coordinates_while_moving_right(coordinates[index-1][0], coordinates[index-1][1], row_and_col[0], row_and_col[1])

                            board = copy.deepcopy(board_original_state)
                            for index, value in enumerate(coordinates[::1]):
                                board[value[0]][value[1]] = index

                            board[H_row][H_col] = "H"
                            board_tail_visited[_9_row][_9_col] = 1

                    elif direction == "U":
                        # for move in range(moves_number):
                        raise NotImplementedError

                            # H_row -= 1
                            #
                            # if H_row - T_row < - 1:
                            #     T_row -= 1
                            #
                            #     if H_col - T_col > 0:
                            #         T_col += 1
                            #
                            #     elif H_col - T_col < 0:
                            #         T_col -= 1
                            #
                            # # board = copy.deepcopy(board_original_state)
                            #
                            # board[H_row][H_col] = "H"
                            # board[T_row][T_col] = "T"
                            # board_tail_visited[T_row][T_col] = 1

                    elif direction == "L":
                        raise NotImplementedError
                        # for move in range(moves_number):
                        #
                        #     H_col -= 1
                        #
                        #     if H_col - T_col < -1:
                        #         T_col -= 1
                        #
                        #         if H_row - T_row > 0:
                        #             T_row += 1
                        #         elif H_row - T_row < 0:
                        #             T_row -= 1
                        #
                        #     # board = copy.deepcopy(board_original_state)
                        #
                        #     board[H_row][H_col] = "H"
                        #     board[T_row][T_col] = "T"
                        #     board_tail_visited[T_row][T_col] = 1

                    elif direction == "D":
                        raise NotImplementedError
                        # for move in range(moves_number):
                        #
                        #     H_row += 1
                        #
                        #     if H_row - T_row > 1:
                        #         T_row += 1
                        #
                        #         if H_col - T_col > 0:
                        #             T_col += 1
                        #
                        #         elif H_col - T_col < 0:
                        #             T_col -= 1
                        #
                        #     # board = copy.deepcopy(board_original_state)
                        #
                        #     board[H_row][H_col] = "H"
                        #     board[T_row][T_col] = "T"
                        #     board_tail_visited[T_row][T_col] = 1


                except Exception as e:
                    print(e)
                    print(line_number, line)
            result = 0
            for row in board_tail_visited:
                result += sum(row)
            return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        self.assertEqual(13, Solution().fuction("09_input_test_2.txt", 12))

    def test_prod(self):
        self.assertEqual(6181, Solution().fuction("09_input.txt", 1000))
