import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self) -> None:
        self.g1 = Guess('apple')
    
    def tearDown(self) -> None:
        pass
    
    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_, _, _, _, _')

        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), 'a, _, _, _, _')
        self.g1.guess('p')
        self.assertEqual(self.g1.displayCurrent(), 'a, p, p, _, _')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'a, p, p, l, _')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), 'a, p, p, l, e')

        self.g1.guess('x')
        self.assertEqual(self.g1.displayCurrent(), 'a, p, p, l, e')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), 'Nothing')

        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), 'a')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), 'a, e')
        self.g1.guess('p')
        self.assertEqual(self.g1.displayGuessed(), 'a, e, p')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), 'a, e, l, p')

        self.g1.guess('x')
        self.assertEqual(self.g1.displayGuessed(), 'a, e, l, p, x')

    def testGuess(self):
        self.g1.guess('y')
        self.assertEqual(self.g1.currentStatus, {})

        self.g1.guess('p')
        self.assertEqual(self.g1.currentStatus, {'p':[1, 2]})
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, {'a': [0], 'p':[1, 2]})
        self.g1.guess('l')
        self.assertEqual(self.g1.currentStatus, {'a': [0], 'p':[1, 2], 'l': [3]})
        self.g1.guess('e')
        self.assertEqual(self.g1.currentStatus, {'a': [0], 'p':[1, 2], 'l': [3], 'e': [4]})

        self.g1.guess('x')
        self.assertEqual(self.g1.currentStatus, {'a': [0], 'p':[1, 2], 'l': [3], 'e': [4]})

        self.assertTrue(self.g1.guess('p'))
        self.assertFalse(self.g1.guess('x'))

    def testCheckClear(self):
        self.g1.guessedChars.update(['a', 'p'])
        self.assertFalse(self.g1.check_clear())
        
        self.g1.guessedChars.update(['a', 'e', 'l', 'p'])
        self.assertTrue(self.g1.check_clear())
        self.g1.guessedChars.update(['a', 'e', 'l', 'p', 'x', 'y', 'z'])
        self.assertTrue(self.g1.check_clear())

if __name__ == '__main__':
    unittest.main()