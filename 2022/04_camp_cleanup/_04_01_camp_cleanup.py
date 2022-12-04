"""
Plan:
read in 1 line
split by ,
a-b, y,z

y      z
   ab

a      b
    yz

y<a and b<z
OR
a<y and z<b


"""

"""
Docs:

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

                if (y <= a and b <= z) or (a <= y and z <= b):
                    result += 1

        print(result)
        return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().camp_cleanup("04_input_test.txt") == 2

    def test_prod(self):
        assert Solution().camp_cleanup("04_input.txt") == 503
