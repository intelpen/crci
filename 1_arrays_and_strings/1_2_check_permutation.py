# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Solution ideea:  to be a permutation they need to have the same elements with the same counts
# Filter : check same number of elements
# 1. One brute force : sort the 2( O(n log n)) and compare sorted arrays O(n)
# 2. Count all elements in a hash (o(n) and compare them - o(n))
#3. use 2 stacks - o(n) -> add a pair of elements each time and remove when empty o(n)

import unittest

def count_chars(in_str):
    if in_str is None:
        return {}
    counts_dict = {}
    for character in in_str:
        counts_dict[character] = counts_dict.get(character, 0) +1
    print(f"string:{in_str} counts {counts_dict}")
    return counts_dict

def check_permutation_with_dict(first_str, second_str):
    return count_chars(first_str) == count_chars(second_str)

def check_permutation_with_sort(first_str,second_str):
    if first_str is None:
        return first_str == second_str
    else:
        return sorted(first_str) == sorted(second_str)

class TestCheckPermutation(unittest.TestCase):
    tests_dict = {("aba", "baa"):True, ("oua", "uuu"):False, ("", ""):True, (None, "a"): False}
    def run_checks(self, function_to_test):
        for strings_pair in self.tests_dict:
            assert function_to_test(strings_pair[0], strings_pair[1]) == self.tests_dict[strings_pair]
    def test_check_permutation_with_dict(self):
        self.run_checks(check_permutation_with_dict)

    def test_check_permutation_with_sort(self):
        self.run_checks(check_permutation_with_sort)