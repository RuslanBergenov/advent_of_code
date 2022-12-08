"""
Plan:
recursion
read into a nested dict
compute all dirs sizes
calculate the answer

"""

"""
Docs:
https://www.w3schools.com/python/python_regex.asp
https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match#:~:text=on%20this%20post.-,re.,until%20it%20finds%20a%20match.&text=Save%20this%20answer.,-Show%20activity%20on
"""

import unittest
import re

class Solution(object):
    # def read_input(self, file_name):
    #     #     lines = []
    #     #     with open(file_name) as f:
    #     #         for line in f:
    #     #             lines.append(line)
    #     #     return lines
    #     # #
    #     # # def calculate_size(self, line):
    #     # #     if "$ dir" in line:
    #     # #     elif line == "$ cd ..":
    #     # #     elif




    def calculate_total_sizes(self, file_name):

        folders_names_stack = []
        folders_stack = []
        parent_folder_name = None
        with open(file_name) as f:

            for line in f:
                if "$ cd" in line and line != "$ cd ..\n":

                    if len(folders_stack) > 0:
                        parent_folder_name = current_folder_name

                    current_folder_name = re.match(r'\$ cd (.?)$', line).group(1)

                    current_folder = {current_folder_name: []}

                    folders_stack.append(current_folder)
                    folders_names_stack.append(current_folder_name)
                elif "$ ls" in line:
                    continue
                elif "dir" in line:
                    subfolder_name = re.match(r'dir (.?)$', line).group(1)
                    subfolder = {subfolder_name: []}
                    current_folder[current_folder_name].append(subfolder)
                elif "$ cd .." in line:
                    folders_stack.pop()
                    current_folder = folders_stack[-1]
                elif bool(re.match(r'^[0-9]+', line)):
                    file_size =  re.match(r'^[0-9]+', line).group()
                    current_folder[current_folder_name].append(int(file_size))

#TODO: how do I merge the dictionaries?


class TestCase(unittest.TestCase):

    def test_dev(self):
        input=Solution().calculate_total_sizes("07_input_test.txt")
        assert Solution().calculate_total_sizes(input) == 0
    #
    # def test_prod(self):
    #     assert Solution().solution("07_input.txt") == 1
