# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
import unittest

def is_unique_with_set(in_str):
    return len(in_str) == len(set(in_str))
class TestIsUnique(unittest.TestCase):
    def test_is_unique(self):
        self.assertFalse(is_unique_with_set("abcda"))
        self.assertTrue(is_unique_with_set("abcA"))
        self.assertTrue(is_unique_with_set("abc"))

if __name__ == '__main__':
    unittest.main()