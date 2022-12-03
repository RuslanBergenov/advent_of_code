"""
https://adventofcode.com/2022/day/3
Day 3
Read in line
Split line into 2 parts
Create two sets
Set intersect
ASCII
Convert to score(s)
Increment running total


If ord(X)

65-90?
65-38=27

97-122?
97-96=1

What if length of input is odd number???
"""

"""
Docs
https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

https://medium.com/interview-buddy/handling-ascii-character-in-python-58993859c38e
"""

import unittest


class Solution(object):
    def rucksack(self, file_name):
        result = 0
        with open(file_name) as f:
            for line in f:
                length = len(line)

                rucksack_left = line[0:length // 2]
                rucksack_right = line[length // 2:length]
                list_left = [*rucksack_left]
                list_right = [*rucksack_right]
                set_left = set(list_left)
                set_right = set(list_right)

                common_items = set_left.intersection(set_right)

                for item in common_items:
                    ascii_code = ord(item)

                    if 97 <= ascii_code <= 122:
                        result += (ascii_code - 96)
                    elif 65 <= ascii_code <= 90:
                        result += (ascii_code - 38)
        print(f"result: {result}")
        return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().rucksack("03_input_test.txt") == 157

    def test_prod(self):
        assert Solution().rucksack("03_input.txt") == 8072
