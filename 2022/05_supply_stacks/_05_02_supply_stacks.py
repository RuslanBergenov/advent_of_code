"""
Plan:
read input into stacks
parse instructions
execute instructions
"""

"""
Docs:

"""

import re
from itertools import islice

import unittest


class Solution(object):
    def supply_stacks(self, file_name):
        result = ""

        # read in data and create stacks
        with open(file_name) as f:
            rows = []
            for line in f:
                if "[" not in line:
                    break
                row = line.replace("    ", "[]")
                letters = re.findall(r'\[(.*?)\]', row)
                rows.append(letters)
        stacks = []
        for i in range(0, len(rows[-1])):
            stacks.append([])
        for i in range(0, len(rows[-1])):
            for index, value in enumerate(rows):
                try:
                    if len(value[i]) > 0:\
                        stacks[i].append(value[i])
                except Exception as e:
                    print(e)
        for stack in stacks:
            stack.reverse()

        # move crates
        with open(file_name) as f:
            for line in islice(f, len(rows)+2, None):
                number_of_crates = int(re.search(r'move (.*?) from', line).group(1))
                source = int(re.search(r'from (.*?) to', line).group(1))
                destination = int(re.search(r'to (.*?)$', line).group(1))
                temp = []
                for crate in range(0, number_of_crates):
                    temp.append(stacks[source - 1].pop())
                temp.reverse()
                stacks[destination-1].extend(temp)

        # create result
        for stack in stacks:
            result += stack.pop()
        print(f"result: {result}")
        return result

class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().supply_stacks("05_input_test.txt") == "MCD"

    def test_prod(self):
        assert Solution().supply_stacks("05_input.txt") == "RWLWGJGFD"
