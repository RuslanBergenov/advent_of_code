# https://adventofcode.com/2022/day/2

"""
A 1st player rock
B 1st player paper
C 1st player scissors

X 2nd player rock
Y 2nd player paper
Z 2nd player scissors


rock        1
paper       2
scissors    3

victory     6

winning combinations for 2nd player:
A Y
B Z
C X
"""


import unittest

class Solution(object):
    def rock_paper_scissors(self, file_name):
        moves_mapping = {"A": "X",
                         "B": "Y",
                         "C": "Z"}

        winning_combinations = {"A Y",
                                "B Z",
                                "C X"}
        participation_scores = {"X": 1,
                                "Y": 2,
                                "Z": 3}
        score = 0
        with open(file_name) as f:
            i = 0
            for line in f:
                i+=1
                print(line)

                line_cleaned = line.replace("\n","")
                if line_cleaned in winning_combinations:
                    score += 6
                my_move = line_cleaned.split()[1]
                oppenents_move_translated = moves_mapping[line_cleaned.split()[0]]

                score += participation_scores[my_move]

                if my_move == oppenents_move_translated:
                    score += participation_scores[my_move]

        print(score)
        print("lines:", i)
        return score







class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().rock_paper_scissors("02_input_test.txt") == 15

    def test_prod(self):
        assert Solution().rock_paper_scissors("02_input.txt") == 12992

