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

    def fuction(self, file_name, board_number_of_rows, board_row_length, starting_point_row, starting_point_column):
        board = []

        for i in range(board_number_of_rows):
            row = []
            for j in range(board_row_length):
                row.append(0)
            board.append(row)
        board_tail_visited = copy.deepcopy(board)
        board[starting_point_row][starting_point_column] = "s"
        board_original_state = copy.deepcopy(board)

        coordinates = []

        x_start = starting_point_row
        y_start = starting_point_column

        for i in range(10):
            coordinates.append([x_start, y_start])

        board[coordinates[0][0]][coordinates[0][1]] = "H"

        pass

        def move_right(leader_row, leader_column, follower_row, follower_column):
            if leader_column - follower_column > 1 or abs(leader_row - follower_row) > 1:
                follower_column += 1

                if leader_row - follower_row > 0:
                    follower_row += 1
                elif leader_row - follower_row < 0:
                    follower_row -= 1
            return follower_row, follower_column

        def move_up(leader_row, leader_column, follower_row, follower_column):
            if leader_row - follower_row < - 1 or abs(leader_column - follower_column) > 1:

                follower_row -= 1

                if leader_column - follower_column > 0:
                    follower_column += 1

                elif leader_column - follower_column < 0:
                    follower_column -= 1
            return follower_row, follower_column

        def move_left(leader_row, leader_column, follower_row, follower_column):
            if leader_column - follower_column < -1 or abs(leader_row - follower_row) > 1:
                follower_column -= 1

                if leader_row - follower_row > 0:
                    follower_row += 1
                elif leader_row - follower_row < 0:
                    follower_row -= 1
            return follower_row, follower_column

        def move_down(leader_row, leader_column, follower_row, follower_column):
            if leader_row - follower_row > 1 or abs(leader_column - follower_column) > 1:
                follower_row += 1

                if leader_column - follower_column > 0:
                    follower_column += 1

                elif leader_column - follower_column < 0:
                    follower_column -= 1
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

                            for index, row_and_col in enumerate(coordinates[1:]):
                                if index == 0:
                                    continue
                                coordinates[index][0], coordinates[index][1] = move_right(coordinates[index - 1][0],
                                                                                          coordinates[index - 1][1],
                                                                                          coordinates[index][0],
                                                                                          coordinates[index][1])

                            board = copy.deepcopy(board_original_state)

                            for index, value in enumerate(coordinates[::-1]):
                                board[value[0]][value[1]] = 9 - index

                            board[coordinates[0][0]][coordinates[0][1]] = "H"
                            board_tail_visited[coordinates[9][0]][coordinates[9][1]] = 1

                    elif direction == "U":
                        for move in range(moves_number):

                            coordinates[0][0] -= 1

                            for index, row_and_col in enumerate(coordinates):
                                if index == 0:
                                    continue
                                coordinates[index][0], coordinates[index][1] = move_up(coordinates[index - 1][0],
                                                                                       coordinates[index - 1][1],
                                                                                       coordinates[index][0],
                                                                                       coordinates[index][1])

                            board = copy.deepcopy(board_original_state)

                            for index, value in enumerate(coordinates[::-1]):
                                board[value[0]][value[1]] = 9 - index

                            board[coordinates[0][0]][coordinates[0][1]] = "H"
                            board_tail_visited[coordinates[9][0]][coordinates[9][1]] = 1

                    elif direction == "L":
                        for move in range(moves_number):

                            coordinates[0][1] -= 1

                            for index, row_and_col in enumerate(coordinates):
                                if index == 0:
                                    continue
                                coordinates[index][0], coordinates[index][1] = move_left(coordinates[index - 1][0],
                                                                                         coordinates[index - 1][1],
                                                                                         coordinates[index][0],
                                                                                         coordinates[index][1])

                            board = copy.deepcopy(board_original_state)

                            for index, value in enumerate(coordinates[::-1]):
                                board[value[0]][value[1]] = 9 - index

                            board[coordinates[0][0]][coordinates[0][1]] = "H"
                            board_tail_visited[coordinates[9][0]][coordinates[9][1]] = 1

                    elif direction == "D":

                        for move in range(moves_number):

                            coordinates[0][0] += 1

                            for index, row_and_col in enumerate(coordinates):
                                if index == 0:
                                    continue
                                coordinates[index][0], coordinates[index][1] = move_down(coordinates[index - 1][0],
                                                                                         coordinates[index - 1][1],
                                                                                         coordinates[index][0],
                                                                                         coordinates[index][1])

                            board = copy.deepcopy(board_original_state)

                            for index, value in enumerate(coordinates[::-1]):
                                board[value[0]][value[1]] = 9 - index

                            board[coordinates[0][0]][coordinates[0][1]] = "H"
                            board_tail_visited[coordinates[9][0]][coordinates[9][1]] = 1


                except Exception as e:
                    print(e)
                    print(line_number, line)
            result = 0
            for row in board_tail_visited:
                result += sum(row)
            return result


class TestCase(unittest.TestCase):

    # def test_dev_0(self):
    #     self.assertEqual(1, Solution().fuction(file_name="09_input_test.txt", board_number_of_rows=5, board_row_length=6,
    #                                            starting_point_row=4, starting_point_column=0))

    def test_dev_1(self):
        self.assertEqual(36, Solution().fuction(file_name="09_input_test_2.txt", board_number_of_rows=21,
                                                board_row_length=26,
                                                starting_point_row=15, starting_point_column=11))

    # def test_prod(self):
    #     self.assertEqual(6181, Solution().fuction("09_input.txt", 1000))
