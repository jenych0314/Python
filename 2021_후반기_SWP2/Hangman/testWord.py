import unittest

from word import Word

class TestGuess(unittest.TestCase):

    def setUp(self) -> None:
        self.g1 = Word('C:/Users/jeony/OneDrive/바탕 화면/Python/CLASS/Hangman/words.txt')
    
    def tearDown(self) -> None:
        pass
    
    def testInit(self):
        self.assertFalse(self.g1.count == 0)
        self.assertFalse(len(self.g1.words) == 0)

if __name__ == '__main__':
    unittest.main()