from hangman import Hangman
from guess import Guess
from word import Word
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QTextEdit, QToolButton, QWidget
from PyQt5.QtCore import Qt

class HangmanGame(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.initUI()
        self.startGame()
    
    def initUI(self): # UI 컴포넌트 생성/배치
        # hangmanLayout
        hangmanLayout = QGridLayout()

        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # statusLayout
        statusLayout = QGridLayout()

        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        self.guessButton = QToolButton()
        self.guessButton.setText('Guess')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        self.newButton = QToolButton()
        self.newButton.setText('New Game')
        self.newButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newButton, 4, 0)

        # mainLayout
        mainLayout = QGridLayout()
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        # all
        self.setLayout(mainLayout)
        self.setWindowTitle('Hangman Game')
        self.setGeometry(300, 300, 800, 250)
        self.show()

    def startGame(self): # 게임 초기화
        self.word = Word('words.txt') # words list 초기화
        self.hangman = Hangman() # hangman 상태 초기화 (남은 목숨: 최대치)
        self.guess = Guess(self.word.randFromDB(3)) # 비밀 단어 선택
        self.gameOver = False # 게임이 진행 중인지 여부를 나타내는 플래그 초기화

        # 각 표시 창에 알맞은 내용 표시
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent()) # currentWord
        self.guessedChars.setText(self.guess.displayGuessed()) # guessedChars
        self.message.clear() # message
    
    def guessClicked(self): # 사용자 입력 처리
        guessedChar = self.charInput.text() # 사용자가 입력한 글자를 받아들임
        self.charInput.clear()
        self.message.clear()
        
        if self.gameOver == True: # 게임 진행 중인지를 판단: 아니라면, 메시지만 출력
            # 메시지 출력하고 (message.setText) 리턴
            string = 'Please click the New Game'
            self.message.setText(string)
        else:
            if guessedChar.isalpha():
                # 입력의 길이가 1인지를 판단하고, 아닌 경우 메시지 출력, 리턴
                if len(guessedChar) != 1:
                    string = 'One character at a time!'
                # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
                elif guessedChar in self.guess.guessedChars:
                    string = f'You already guessed \"{guessedChar}\"'
            else: # 영어 외에 다른 문자를 입력했을 때
                string = 'Enter the English only'

            success = self.guess.guess(guessedChar) # 입력 받은 글자를 이용해서 Guess.guess() 메서드를 호출

            if success == False: # - 만약 리턴 값이 False이면: 메시지 출력, 목숨을 1만큼 감소
                string = f'There\'s no {guessedChar}'
                self.message.setText(string)
                self.hangman.decreaseLife() # 남아 있는 목숨을 1만큼 감소
                # 메시지 출력

            # 상태 표출: hangmanWindow, currentWord, guessedChars
            # hangmanWindow에 현재 hangman 상태 그림을 출력
            string = self.hangman.currentShape()
            self.hangmanWindow.setText(string)
            # currentWord에 현재 부분 맞추어진 단어 상태를 출력
            string = self.guess.displayCurrent()
            self.currentWord.setText(string)
            # guessedChars에 지금까지 이용한 글자들의 집합을 출력
            string = self.guess.displayGuessed()
            self.guessedChars.setText(string)

            if self.guess.check_clear(): # 단어 전체를 맞추었는지 판단
                # 메시지 ('Success!') 출력하고, self.gameOver <- True
                # - 그렇다면, 메시지 출력하고 게임 진행 중 상태는 'Game Over'
                string = 'Success!'
                self.message.setText(string)
                self.gameOver = True
            elif self.hangman.getRemainingLives() == 0: # 목숨이 소진되었는지를 판단
                # - 그렇다면, 메시지 출력하고 게임 진행 중 상태는 'Game Over'
                # 메시지 ('Fail' + 비밀 단어) 출력하고, self.gameOver <- True
                string = f'Fail, word [{self.guess.secretWord}]'
                self.message.setText(string)
                self.gameOver = True

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    sys.exit(app.exec_())