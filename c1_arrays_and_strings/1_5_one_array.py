# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# Solution : combine a fird first dif cu equal for the re rest
import unittest

def one_away(first_str, second_str):
    len_first = len(first_str)
    len_second = len(second_str)
    if abs(len_first - len_second) >1:
        return False
    for i in range(min(len_first,len_second)):
        if first_str[i] == second_str[i]:
            i+=1
        else:
            break
    if i == len_first-1:
        return True
    else:
        if len_first == len_second:
            return first_str[i+1:] == second_str[i+1:]
        else:
            #if first longer , so one remove
            if len_first == len_second +1:
                return first_str[i+1:] == second_str[i:]
            else:
                #second_str longer
                return second_str[i + 1:] == first_str[i:]

class TestOneAway(unittest.TestCase):
    tests_dict = {
        ("pale", "ple"):True,
        ("pales", "pale"): True,
        ("pale", "bale"): True,
        ("pale", "bake"): False
    }
    def run_tests(self, function_to_test):
        for test_example in self.tests_dict:
            assert function_to_test(test_example[0],test_example[1]) == self.tests_dict[test_example]

    def test_one_away(self):
        self.run_tests(one_away)
