"""
https://adventofcode.com/2022/day/1
https://adventofcode.com/2022/day/1/input

read input into a list of lists
reduce each list to its today
get the max total
"""

import unittest
import os

class Solution(object):
    def count_calories(self, file_name):
        """

        :param file_name:
        :return:
        """
        elves_and_calories = []

        file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file_name))

        file = open(file_path, "r")

        # https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
        elf_calories = []
        for calorie_amount in file:

            if calorie_amount == "\n":
                elves_and_calories.append(elf_calories)
                elf_calories = []
            else:
                elf_calories.append(int(calorie_amount.replace("/n", "")))

        # The "for-else" design
        # https://stackoverflow.com/questions/10140281/how-to-find-out-whether-a-file-is-at-its-eof
        # https://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
        else:
            elves_and_calories.append(elf_calories)
        file.close()

        calories_for_each_elf = []
        for elfs_calories in elves_and_calories:
            calories_for_each_elf.append(sum(elfs_calories))
        # sort sorts in place
        # sorted returns a sorted list
        calories_for_each_elf.sort(reverse=True)
        ans = sum(calories_for_each_elf[0:3])
        print(ans)
        return ans


class TestCase(unittest.TestCase):
    def test_function_0(self):
        assert Solution().count_calories("01_calorie_counting/day01_calorie_counting_test.txt") == 45000

    def test_function_1(self):
        assert Solution().count_calories("01_calorie_counting/day01_calorie_counting.txt") == 208437



