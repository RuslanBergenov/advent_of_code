import unittest


class Solution(object):

    def parse_input(self, file_name):
        with open(file_name) as f:
            first_line = f.readline()
        return first_line

    def function(self, min_char, string):
        for i in range(min_char - 1, len(string)):
            left = i - (min_char - 1)
            right = i
            substring = string[left:right + 1]
            if sorted(list(substring)) == sorted(list(set(substring))):
                ans = right + 1
                print("answer:", ans)
                return ans


class TestCasePart1(unittest.TestCase):
    min_char = 4
    input = Solution().parse_input("06_input.txt")

    def test_dev(self):
        self.assertEqual(7, Solution().function(self.min_char, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"))

    def test_prod(self):
        self.assertEqual(1707, Solution().function(self.min_char, self.input))


class TestCasePart2(unittest.TestCase):
    min_char = 14
    input = Solution().parse_input("06_input.txt")

    def test_dev(self):
        self.assertEqual(19, Solution().function(self.min_char, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"))

    def test_prod(self):
        self.assertEqual(3697, Solution().function(self.min_char, self.input))
