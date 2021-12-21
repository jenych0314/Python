import unittest

from palindrome3 import Palindrome3

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.p1 = Palindrome3('abcd')
        self.p2 = Palindrome3('abcdedcba')
        self.p3 = Palindrome3('ab c d cba')
    
    def tearDown(self):
        pass
    
    def test_normal(self):
        self.assertFalse(self.p1.normal())
        self.assertTrue(self.p2.normal())
        self.assertFalse(self.p3.normal())
    
    def test_recursive(self):
        self.assertFalse(self.p1.recursive())
        self.assertTrue(self.p2.recursive())
        self.assertFalse(self.p3.recursive())
    
    def test_ignore_spaces(self):
        self.assertFalse(self.p1.ignoreSpaces())
        self.assertTrue(self.p2.ignoreSpaces())
        self.assertTrue(self.p3.ignoreSpaces())

if __name__ == '__main__':
    unittest.main()