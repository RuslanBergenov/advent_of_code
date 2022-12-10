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

        coordinates = []
        for i in range(10):
            coordinates.append([s, s])


        def move_right(leader_row, leader_column, follower_row, follower_column):

            if leader_column - follower_column > 1:
                follower_column += 1

                if leader_row - follower_row > 0:
                    follower_row += 1
                elif leader_row - follower_row < 0:
                    follower_row -= 1
            return follower_row, follower_column

        line_number = 0
        with open(file_name) as f:
            for line in f:
                line_number += 1
                try:
                    direction = line.split()[0]
                    moves_number = int(line.split()[1])

                    if direction == "R":

                        for move in range(moves_number):

                            coordinates[0][1] += 1

                            for index, row_and_col in enumerate(coordinates):
                                coordinates[index][0], coordinates[index][1] = move_right(coordinates[index-1][0], coordinates[index-1][1], coordinates[index][0], coordinates[index][1])

                            board = copy.deepcopy(board_original_state)
                            # for index, value in enumerate(coordinates):
                            for index, value in enumerate(coordinates[::-1]):
                                board[value[0]][value[1]] = 9-index

                            board[coordinates[0][0]][coordinates[0][1]] = "H"
                            board_tail_visited[coordinates[9][0]][coordinates[9][1]] = 1

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

    def test_dev_0(self):
        self.assertEqual(13, Solution().fuction("09_input_test.txt", 12))

    # def test_dev_1(self):
    #     self.assertEqual(13, Solution().fuction("09_input_test_2.txt", 12))
    #
    # def test_prod(self):
    #     self.assertEqual(6181, Solution().fuction("09_input.txt", 1000))
