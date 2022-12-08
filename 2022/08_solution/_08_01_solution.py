"""
Plan:
"""

"""
Docs:

"""

import unittest



def solution(file_name):

    forest = []
    with open(file_name) as f:
        for row in f:
            forest.append(list(row.replace("\n", "")))
    result = 0
    for irow, vrow in enumerate(forest):
        for itree, vtree in enumerate(forest[irow]):
            if irow == 0 or irow == len(forest) - 1 or itree == 0 or itree == len(row) - 1:
                result += 1

            else:

                nb_left = forest[irow][0:itree]
                nb_right = forest[irow][itree+1:]

                nb_above = []
                for irow_above in range(0, irow):
                    nb_above.append(forest[irow_above][itree])
                nb_below = []
                for ir_below in range(irow + 1, len(forest)):
                    nb_below.append(forest[ir_below][itree])

                if vtree > max(nb_left) or vtree > max(nb_right) or vtree > max(nb_above) or vtree > max(nb_below):
                    result += 1

    return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        self.assertEqual(21, solution("08_input_test.txt"))

    def test_prod(self):
        self.assertEqual(21, solution("08_input.txt"))
