"""
Docs
https://stackoverflow.com/questions/18422127/python-read-text-file-from-second-line-to-fifteenth
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
