"""
Docs:
https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
"""

import unittest


class Solution(object):
    def camp_cleanup(self, file_name):
        result = 0
        with open(file_name) as f:
            for line in f:

                pair = line.split(",")

                elf_1 = pair[0]
                elf_2 = pair[1]

                elf_1_bounds = elf_1.split("-")
                elf_2_bounds = elf_2.split("-")

                a, b = int(elf_1_bounds[0]), int(elf_1_bounds[1])
                y, z = int(elf_2_bounds[0]), int(elf_2_bounds[1])

                range_a = set(range(a, b + 1))
                range_b = set(range(y, z + 1))

                intersection = range_a.intersection(range_b)

                if len(intersection) > 0:
                    result += 1

        print(f"result: {result}")
        return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().camp_cleanup("04_input_test.txt") == 4

    def test_dev_2(self):
        assert Solution().camp_cleanup("04_input_test_2.txt") == 0

    def test_prod(self):
        assert Solution().camp_cleanup("04_input.txt") == 827
