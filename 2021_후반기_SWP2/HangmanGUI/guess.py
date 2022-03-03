class Guess:

    def __init__(self, word):
        self.secretWord = word # 비밀 단어
        self.guessedChar = '' # 사용한 글자
        self.guessedChars = set() # 사용한 글자들
        self.currentStatus = {} # 현재 상태

    def displayCurrent(self): # 현재까지 맞춘 글자 상태 return
        temp = ['_' for i in range(len(self.secretWord))]
        for letter, idxes in self.currentStatus.items():
            for i in range(len(idxes)):
                temp[idxes[i]] = letter
        string = ', '.join(temp)
        return string

    def displayGuessed(self): # 현재까지 사용한 글자들 return
        string = ''
        if len(self.guessedChars) == 0:
            string = 'Nothing Yet'
        else:
            temp = sorted(self.guessedChars)
            string = ', '.join(temp)
        return string

    def guess(self, character):
        self.guessedChars.add(character) # 주어진 글자를 사용한 글자의 집합에 원소로 추가

        if character in self.secretWord: # 비밀 단어 안에 있으면 그 위치를 기록 (현재까지 맞춘 글자 상태), true return
            idxes = []
            idx = 0

            while idx < len(self.secretWord):
                idx = self.secretWord.find(character, idx)
                if idx == -1: break
                idxes.append(idx)
                idx += 1
            
            self.currentStatus.setdefault(character, idxes)
            return True
        else: # 없을 경우 false return
            return False
    
    def check_clear(self): # 모든 글자를 다 맞추었으면 True, 그렇지 않으면 False 리턴
        # if len(set(self.secretWord) - set(self.currentStatus.keys())) == 0:
        if len(set(self.secretWord) - self.guessedChars) == 0:
            return True
        else: return False

if __name__ == '__main__':
    string = 'default'
    guess = Guess(string)
    guess.guessedChars.update(['d', 't'])
    print(guess.guessedChars)
    print(guess.check_clear())
    guess.guessedChars.update(['d', 'e', 'f', 'a', 'u', 'l', 't'])
    print(guess.check_clear())
    guess.guessedChars.update(['d', 'e', 'f', 'a', 'u', 'l', 't', 'x', 'y', 'z'])
    print(guess.check_clear())