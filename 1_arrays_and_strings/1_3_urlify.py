# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

# Solution: 1.  copy directly in new list
# Solution2: go one way and count spoaces, then extend the array and add the %20

import unittest

def urlify_with_list(initial_str):
    urlified_list = [character if character != ' ' else "%20" for character in initial_str ]
    print("".join(urlified_list))
    return "".join(urlified_list)

def urlify_from_end(initial_str):
    count_spaces = 0
    for character in initial_str:
        if character == ' ':
            count_spaces +=1
    initial_list=  list(initial_str)
    initial_len = len(initial_list)
    initial_list = initial_list + [None] * count_spaces * 2
    position = len(initial_list)-1
    for position_initial in range(initial_len-1,0,-1):
        if initial_list[position_initial] == ' ':
            initial_list[position]="0"
            initial_list[position-1] = "2"
            initial_list[position-2] = "%"
            position -=3
        else:
            initial_list[position] = initial_list[position_initial]
            position -=1
    return("".join(initial_list))


def replace(initial_str):
    return initial_str.replace(" ", "%20")

class TestUrlify(unittest.TestCase):
    tests_dict = {"ana are mere": "ana are mere".replace(" ", "%20")}

    def run_all_tests(self, function_to_test):
        for test_example, test_result  in self.tests_dict.items():
            assert function_to_test(test_example) == test_result

    def test_urlify_with_list(self):
        self.run_all_tests(urlify_with_list)

    def test_urlify_from_end(self):
        self.run_all_tests(urlify_from_end)

if __name__ == "__main__":
    unittest.main()