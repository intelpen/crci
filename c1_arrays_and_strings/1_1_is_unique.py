# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
import unittest


def is_unique_with_set(in_str):
    return len(in_str) == len(set(in_str))


def is_unique_with_set_second(in_str):
    char_set = set()
    for character in in_str:
        if character not in char_set:
            char_set.add(character)
        else:
            return False
    return True


def is_unique_with_dict(in_str):
    char_dict = {}
    for character in in_str:
        if character not in char_dict:
            char_dict[character] = char_dict.get(character, 0) +1
        else:
            return False
    return True

def is_unique_no_structures(in_str):
    for first_index in range(len(in_str)):
        for second_index in range(first_index+1, len(in_str),1):
            if in_str[first_index] == in_str[second_index]:
                return False
    return True


class TestIsUnique(unittest.TestCase):
    tests_dict = {"abcda": False, "abcA": True, "abc": True}

    def run_tests(self, function_to_test):
        for test_input in self.tests_dict:
            assert function_to_test(test_input) == self.tests_dict[test_input]

    def test_is_unique_with_set(self):
        self.run_tests(is_unique_with_set)

    def test_is_unique_with_set_second(self):
        self.run_tests(is_unique_with_set_second)

    def test_is_unique_with_dict(self):
        self.run_tests(is_unique_with_dict)

    def test_is_unique_no_structures(self):
        self.run_tests(is_unique_no_structures)


if __name__ == '__main__':
    unittest.main()
