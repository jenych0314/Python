import unittest

from palindrome1 import Palindrome1

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.p1 = Palindrome1('abcd')
        self.p2 = Palindrome1('abcdedcba')
    
    def tearDown(self):
        pass
    
    def test_normal(self):
        self.assertFalse(self.p1.normal())
        self.assertTrue(self.p2.normal())

if __name__ == '__main__':
    unittest.main()