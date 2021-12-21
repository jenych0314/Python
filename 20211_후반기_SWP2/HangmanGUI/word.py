import random

class Word:
    
    def __init__(self, filename):
        self.words = []
        self.count = 0
        self.word_length_match_dic = {}
        self.max_length = 0

        try:
            f = open(filename, 'r')
            lines = f.readlines()
            
            for line in lines:
                word = line.rstrip()
                self.words.append(word)
                if not len(word) in self.word_length_match_dic:
                    self.word_length_match_dic[len(word)] = [word]
                else:
                    self.word_length_match_dic[len(word)].append(word)
                self.count += 1

            self.max_length = sorted(list(self.word_length_match_dic.keys()))[-1]

            f.close()
        except:
            print('Error')

    def randFromDB(self, minLength):
        try:
            minLength = min(minLength, self.max_length)
            word_lst = []
            for key, values in sorted(words.word_length_match_dic.items()):
                if key >= minLength:
                    word_lst.append(values)
            return random.choice(random.choice(word_lst))
        except:
            return 'error'

if __name__ == '__main__':
    words = Word('C:/Users/jeony/OneDrive/바탕 화면/Python/CLASS/Hangman/words.txt')
    print(words.randFromDB(5))

    # for key, values in sorted(words.word_length_match_dic.items()):
    #     print(key)
    #     for value in values:
    #         print(value, end = ', ')
    #     print()

    # print(sorted(words.word_length_match_dic.keys())[-1])
    # print(words.max_length)