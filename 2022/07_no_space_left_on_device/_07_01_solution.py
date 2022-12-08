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
import copy





def calculate_file_sizes(file_name):

    with open(file_name) as f:

        folders_and_file_sizes = {}
        folders_stack = []

        for line in f:

            if "$ cd" in line and line != "$ cd ..\n":
                if len(folders_stack) == 0:
                    current_folder_path = "root"

                else:
                    try:
                        current_folder_name = re.match(r'\$ cd (.?)$', line.replace("\n", "")).group()

                    except Exception as e:
                        print(e)
                        print(line)
                        current_folder_name = line.replace("\n", "").split()[2]
                    current_folder_path = folders_stack[-1] + "/" + current_folder_name

                folders_and_file_sizes.update({current_folder_path: 0})
                folders_stack.append(current_folder_path)

            elif "$ cd .." in line:
                folders_stack.pop()

            elif bool(re.match(r'^[0-9]+', line)):
                file_size =  re.match(r'^[0-9]+', line).group()
                folders_and_file_sizes[current_folder_path] += int(file_size)

        return folders_and_file_sizes

def calculate_total_folder_sizes(folders_and_file_sizes):
    total_folder_sizes = copy.deepcopy(folders_and_file_sizes)
    for folder_path, size in folders_and_file_sizes.items():

        for potential_subfolder_path, size in folders_and_file_sizes.items():
            if folder_path!=potential_subfolder_path:
                if potential_subfolder_path.startswith(folder_path):
                    total_folder_sizes[folder_path] += folders_and_file_sizes[potential_subfolder_path]
    return total_folder_sizes


def calculate_answer(total_folder_sizes):
    ans = 0
    for key, value in total_folder_sizes.items():
        if value <= 100000:
            ans+= value
    return ans



class TestCase(unittest.TestCase):

    def test_dev(self):
        input = calculate_file_sizes("07_input_test.txt")
        total_folder_sizes = calculate_total_folder_sizes(input)
        self.assertEqual(95437, calculate_answer(total_folder_sizes))


    def test_prod(self):
        input = calculate_file_sizes("07_input.txt")
        total_folder_sizes = calculate_total_folder_sizes(input)
        self.assertEqual(1432936, calculate_answer(total_folder_sizes))
