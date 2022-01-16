from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()

    while hangman.remainingLives > 0:

        display = hangman.currentShape()
        print(display)
        display = guess.displayCurrent()
        print('Current: ' + display)
        display = guess.displayGuessed()
        print('Already Used: ' + display)
        display = str(hangman.remainingLives)
        print('remaining lives: ' + display)

        guessedChar = input('Select a letter: ')
        if guessedChar.isalpha():
            if len(guessedChar) != 1: # 한 글자를 입력하지 않았을 때
                print('One character at a time!')
                continue
            elif guessedChar in guess.guessedChars: # 이미 입력한 글자일 때
                print('You already guessed \"' + guessedChar + '\"')
                continue
            else: 
                success = guess.guess(guessedChar)
                if not success: # 틀렸을 때
                    hangman.decreaseLife()
        else: # 영어 외에 다른 문자를 입력했을 때
            print('Enter the English only')
            continue

        finished = guess.check_clear()
        if finished == True:
            break

    if finished == True:
        print(guess.secretWord)
        print('****' + guess.displayCurrent() + '****')
        print('Success')
    else:
        print(hangman.currentShape())
        print(f'word [{guess.secretWord}]')
        print(guess.displayCurrent())
        print('Fail')

if __name__ == '__main__':
    gameMain()