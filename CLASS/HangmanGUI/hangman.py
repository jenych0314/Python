class Hangman:

   text = [
      '''\
         ____
      |    |
      |    o
      |   /|\\
      |    |
      |   / \\
      _|_
      |   |______
      |          |
      |__________|\
      ''',

      '''\
         ____
      |    |
      |    o
      |   /|\\
      |    |
      |   /
      _|_
      |   |______
      |          |
      |__________|\
      ''',

      '''\
         ____
      |    |
      |    o
      |   /|\\
      |    |
      |
      _|_
      |   |______
      |          |
      |__________|\
      ''',

      '''\
         ____
      |    |
      |    o
      |   /|
      |    |
      |
      _|_
      |   |______
      |          |
      |__________|\
      ''',

      '''\
         ____
      |    |
      |    o
      |    |
      |    |
      |
      _|_
      |   |______
      |          |
      |__________|\
      ''',

      '''\
         ____
      |    |
      |    o
      |
      |
      |
      _|_
      |   |______
      |          |
      |__________|\
      ''',

      '''\
         ____
      |    |
      |
      |
      |
      |
      _|_
      |   |______
      |          |
      |__________|\
      ''',
   ]

   def __init__(self):
      self.remainingLives = len(self.text) - 1 # 6

   def getRemainingLives(self):
      return self.remainingLives
      
   def currentShape(self):
      return self.text[self.remainingLives]

   def decreaseLife(self):
      self.remainingLives -= 1

if __name__ == '__main__':
   hangman = Hangman()
   print(hangman.currentShape())