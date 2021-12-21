from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [Button(str(x), self.button_clicked) for x in range(0, 10)]

        # . and = Buttons
        self.decButton = Button('.', self.button_clicked)
        self.eqButton = Button('=', self.button_clicked)

        # Operator Buttons
        self.mulButton = Button('*', self.button_clicked)
        self.divButton = Button('/', self.button_clicked)
        self.addButton = Button('+', self.button_clicked)
        self.subButton = Button('-', self.button_clicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.button_clicked)
        self.rparButton = Button(')', self.button_clicked)

        # Clear Button
        self.clearButton = Button('C', self.button_clicked)
        self.backButton = Button('<-', self.button_clicked)

        self.Buttons = [self.digitButton[7], self.digitButton[8], self.digitButton[9], self.mulButton, self.divButton,
                        self.digitButton[4], self.digitButton[5], self.digitButton[6], self.addButton, self.subButton,
                        self.digitButton[1], self.digitButton[2], self.digitButton[3], self.lparButton, self.rparButton,
                        self.digitButton[0], self.decButton, self.eqButton, self.clearButton, self.backButton]
        
        positions = [(i,j) for i in range(4) for j in range(5)]

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        buttonLayout = QGridLayout()

        for position, button in zip(positions, self.Buttons):
            if button == '':
                continue
            buttonLayout.addWidget(button, *position)

        mainLayout.addLayout(buttonLayout, 1, 0)
        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def button_clicked(self):
        try:
            button = self.sender()
            key = button.text()

            if key == '=':
                result = 'Div 0 Error' if '/0' in self.display.text() else str(eval(self.display.text()))
                self.display.setText(result)
            elif key == 'C':
                self.display.setText('')
            elif key == '<-':
                self.display.setText(self.display.text()[:-1])
            else:
                self.display.setText(self.display.text() + key)
        except:
            pass
        
    def keyPressEvent(self, e): # https://freeprog.tistory.com/331
        def isPrintable(key): 
            printable = [ 
            # Qt.Key_Space, 
            Qt.Key_Exclam, # !
            # Qt.Key_QuoteDbl, # "
            # Qt.Key_NumberSign, # #
            # Qt.Key_Dollar, # $
            Qt.Key_Percent, # %
            # Qt.Key_Ampersand, # &
            # Qt.Key_Apostrophe, # '
            Qt.Key_ParenLeft, # (
            Qt.Key_ParenRight, # )
            Qt.Key_Asterisk, # *
            Qt.Key_Plus, # +
            # Qt.Key_Comma, # ,
            Qt.Key_Minus, # -
            Qt.Key_Period, # .
            Qt.Key_Slash, # /
            Qt.Key_0, 
            Qt.Key_1, 
            Qt.Key_2, 
            Qt.Key_3, 
            Qt.Key_4, 
            Qt.Key_5, 
            Qt.Key_6, 
            Qt.Key_7, 
            Qt.Key_8, 
            Qt.Key_9, 
            # Qt.Key_Colon, # :
            # Qt.Key_Semicolon, # ;
            # Qt.Key_Less, # <
            Qt.Key_Equal, # =
            # Qt.Key_Greater, # >
            # Qt.Key_Question, # ?
            # Qt.Key_At, # @
            # Qt.Key_A, 
            # Qt.Key_B, 
            # Qt.Key_C, 
            # Qt.Key_D, 
            # Qt.Key_E, 
            # Qt.Key_F, 
            # Qt.Key_G, 
            # Qt.Key_H, 
            # Qt.Key_I, 
            # Qt.Key_J, 
            # Qt.Key_K, 
            # Qt.Key_L, 
            # Qt.Key_M, 
            # Qt.Key_N, 
            # Qt.Key_O, 
            # Qt.Key_P, 
            # Qt.Key_Q, 
            # Qt.Key_R, 
            # Qt.Key_S, 
            # Qt.Key_T, 
            # Qt.Key_U, 
            # Qt.Key_V, 
            # Qt.Key_W, 
            # Qt.Key_X, 
            # Qt.Key_Y, 
            # Qt.Key_Z, 
            # Qt.Key_BracketLeft, # [
            # Qt.Key_Backslash, # \
            # Qt.Key_BracketRight, # ]
            Qt.Key_AsciiCircum, # ^
            # Qt.Key_Underscore, # _
            # Qt.Key_QuoteLeft, # `
            # Qt.Key_BraceLeft, # {
            # Qt.Key_Bar, # |
            # Qt.Key_BraceRight, # }
            # Qt.Key_AsciiTilde, # ~
            ]

            if key in printable: 
                return True 
            else:
                return False 
        
        control = False 

        # if e.modifiers() & Qt.ControlModifier: 
        #     print('Control') 
        #     control = True 
        # if e.modifiers() & Qt.ShiftModifier: 
        #     print('Shift') 
        # if e.modifiers() & Qt.AltModifier: 
        #     print('Alt') 
        # if e.key() == Qt.Key_Delete:
        #     print('Delete') 
        if e.key() == Qt.Key_Backspace: 
            print('Backspace')
            self.display.setText(self.display.text()[:-1])
        elif e.key() in [Qt.Key_Return, Qt.Key_Enter]: 
            print('Enter')
            result = 'Div 0 Error' if '/0' in self.display.text() else str(eval(self.display.text()))
            self.display.setText(result)
        elif e.key() == Qt.Key_Escape: 
            print('Escape') 
            self.display.setText('')
        # elif e.key() == Qt.Key_Right: 
        #     print('Right') 
        # elif e.key() == Qt.Key_Left: 
        #     print('Left') 
        # elif e.key() == Qt.Key_Up: 
        #     print('Up') 
        # elif e.key() == Qt.Key_Down: 
        #     print('Down') 
        if not control and isPrintable(e.key()):
            print(e.text())
            self.display.setText(self.display.text() + e.text())


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())