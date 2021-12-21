import unittest

from palindrome2 import Palindrome2

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.p1 = Palindrome2('abcd')
        self.p2 = Palindrome2('abcdedcba')
    
    def tearDown(self):
        pass
    
    def test_normal(self):
        self.assertFalse(self.p1.normal())
        self.assertTrue(self.p2.normal())
    
    def test_recursive(self):
        self.assertFalse(self.p1.recursive())
        self.assertTrue(self.p2.recursive())

if __name__ == '__main__':
    unittest.main()