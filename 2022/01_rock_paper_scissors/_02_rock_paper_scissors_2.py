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

X means you need to lose,
Y means you need to end the round in a draw,
Z means you need to win
"""

import unittest


class Solution(object):
    def rock_paper_scissors(self, file_name):

        moves_scores_map = {"rock": 1,
                            "paper": 2,
                            "scissors": 3}

        moves_map = {"X": {"A": "scissors", # lose  # rock - scissors
                           "B": "rock",             # paper - rock
                           "C": "paper"},           # scissors - paper
                     "Y": {"A": "rock",     # draw
                           "B": "paper",
                           "C": "scissors"},
                     "Z": {"A": "paper",     # win  # rock   - paper
                           "B": "scissors",         # paper - scissors
                           "C": "rock"}}            # scissors - rock

        outcomes_score_map = {"X": 0,
                              "Y": 3,
                              "Z": 6}

        score = 0
        with open(file_name) as f:
            for line in f:
                line_cleaned = line.replace("\n", "")
                desired_outcome = line_cleaned.split()[1]
                score += outcomes_score_map[desired_outcome]

                opponents_move = line.split()[0]

                my_move = moves_map[desired_outcome][opponents_move]

                score += moves_scores_map[my_move]

        print(score)

        return score


class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().rock_paper_scissors("02_input_test.txt") == 12

    def test_prod(self):
        assert Solution().rock_paper_scissors("02_input.txt") == 15508
