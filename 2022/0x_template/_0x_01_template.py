"""
Plan:
"""

"""
Docs:

"""

import unittest


class Solution(object):
    def fuction(self, file_name):
        result = 0

        return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        assert Solution().fuction("0x_input_test.txt") == 0

    def test_prod(self):
        assert Solution().fuction("0x_input.txt") == 1
