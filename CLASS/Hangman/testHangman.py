import unittest

from hangman import Hangman

class TestGuess(unittest.TestCase):

    def setUp(self) -> None:
        self.g1 = Hangman()
    
    def tearDown(self) -> None:
        pass
    
    def testInit(self):
        self.assertTrue(self.g1.remainingLives == 6)
    
    def testCurrentShape(self):
        for i in range(6, 0, -1):
            self.g1.decreaseLife()
            self.assertTrue(self.g1.currentShape(), Hangman.text[i])
    
    def testDecreaseLife(self):
        self.g1.decreaseLife()
        self.assertTrue(self.g1.remainingLives == 5)

if __name__ == '__main__':
    unittest.main()