"""
https://adventofcode.com/2022/day/3
Day 3
Read in line
Split line into town parts
Create two sets
Set intersect
ASCII
Convert to score(s)
Increment running total


If Ord(X)

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
        counter = 0

        while True:
            with open(file_name) as f:
                next_group = f.readlines()[counter + 0:counter + 3]
                counter += 3

                if next_group == []:
                    print(f"result: {result}")
                    return result

                elf_1_list = [*next_group[0]]
                elf_2_list = [*next_group[1]]
                elf_3_list = [*next_group[2]]

                set_1 = set(elf_1_list)
                set_2 = set(elf_2_list)
                set_3 = set(elf_3_list)

                common_items_1_2 = set_1.intersection(set_2)
                common_items = common_items_1_2.intersection(set_3)

                for item in common_items:
                    ascii_code = ord(item)

                    if 97 <= ascii_code <= 122:
                        result += (ascii_code - 96)
                    elif 65 <= ascii_code <= 90:
                        result += (ascii_code - 38)



class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().rucksack("03_input_test.txt") == 70

    def test_prod(self):
        assert Solution().rucksack("03_input.txt") == 2567
