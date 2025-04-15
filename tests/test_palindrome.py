import unittest
from src.is_palindrome import is_palindrome
class TestPalindrome(unittest.TestCase):

    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

if __name__ == '__main__':
    unittest.main()