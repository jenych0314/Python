import random

class Word:
    
    def __init__(self, filename):
        self.words = []
        self.count = 0
        
        try:
            f = open(filename, 'r')
            lines = f.readlines()
            
            for line in lines:
                word = line.rstrip()
                self.words.append(word)
                self.count += 1

            f.close()
        except:
            print('Error')

    def randFromDB(self):
        try:
            r = random.randrange(self.count)
            return self.words[r]
        except:
            return 'error'

if __name__ == '__main__':
    words = Word('C:/Users/jeony/OneDrive/바탕 화면/Python/CLASS/Hangman/words.txt')
    print(words.test())
    print(words.randFromDB())