"""
Plan:
"""

"""
Docs:
https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
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

            nb_left = forest[irow][0:itree]
            nb_right = forest[irow][itree+1:]

            nb_above = []
            for irow_above in range(0, irow):
                nb_above.append(forest[irow_above][itree])
            nb_below = []
            for ir_below in range(irow + 1, len(forest)):
                nb_below.append(forest[ir_below][itree])

            # current_tree_score = 0
            #  left and above - reverse
            score_left = 0
            for index_neighbor, value_neighbor in enumerate(nb_left[::-1]):
                if vtree > value_neighbor:
                    score_left += 1
                elif vtree <= value_neighbor:
                    score_left += 1
                    break

            score_above = 0
            for index_neighbor, value_neighbor in enumerate(nb_above[::-1]):
                if vtree > value_neighbor:
                    score_above += 1
                elif vtree <= value_neighbor:
                    score_above += 1
                    break

            score_right = 0
            for index_neighbor, value_neighbor in enumerate(nb_right):
                if vtree > value_neighbor:
                    score_right += 1
                elif vtree <= value_neighbor:
                    score_right += 1
                    break

            score_below = 0
            for index_neighbor, value_neighbor in enumerate(nb_below):
                if vtree > value_neighbor:
                    score_below += 1
                elif vtree <= value_neighbor:
                    score_below += 1
                    break
            current_tree_score = score_left * score_above * score_right * score_below
            result = max(result, current_tree_score)


    return result


class TestCase(unittest.TestCase):

    def test_dev(self):
        self.assertEqual(8, solution("08_input_test.txt"))

    def test_prod(self):
        self.assertEqual(440640, solution("08_input.txt"))
