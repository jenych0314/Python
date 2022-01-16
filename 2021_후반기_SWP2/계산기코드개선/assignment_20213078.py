from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from myButton import *
from keypad import *
from calcFunction import *
from functions import *
from constants import *

class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        numLayout = QGridLayout()
        operatorLayout = QGridLayout()
        constantLayout = QGridLayout()
        functionLayout = QGridLayout()

        buttonGroups = {
            'num':{'buttons': numPadList, 'layout': numLayout, 'columns':3},
            'operator':{'buttons': operatorList, 'layout': operatorLayout, 'columns':2},
            'constant':{'buttons': constantList, 'layout': constantLayout, 'columns':1},
            'function':{'buttons': functionList, 'layout': functionLayout, 'columns':1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for buttonText in buttonPad['buttons']:
                button = Button(buttonText, self.button_clicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(operatorLayout, 1, 1)
        mainLayout.addLayout(constantLayout, 2, 0)
        mainLayout.addLayout(functionLayout, 2, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")

    def button_clicked(self):
        button = self.sender()
        key = button.text()

        self.clear_text()

        if key == '=': # evaluation
            try:
                result = str(eval(self.display.text()))
            # except ZeroDivisionError:
            #     result = 'Div 0 Error'
            # except ValueError:
            #     result = 'ValueError'
            # except IndexError:
            #     result = 'IndexError'
            except:
                result = 'Error'
            self.display.setText(result)
        elif key == 'C': # clear
            self.display.setText('')
        elif key == '<-': # back
            self.display.setText(self.display.text()[:-1])
        elif key in constantList: # constant
            for k in constantDic.keys():
                if key == k:
                    self.display.setText(self.display.text() + constantDic[key])
                    break
        elif key in functionList: # function
            for k in functionDic.keys():
                if key == k:
                    try:
                        n = self.display.text()
                        value = functionDic[key](n)
                        self.display.setText(str(value))
                    # except ZeroDivisionError:
                    #     self.display.setText('Div 0 Error')
                    # except ValueError:
                    #     self.display.setText('ValueError')
                    # except IndexError:
                    #     self.display.setText('IndexError')
                    except:
                        self.display.setText('Error')
                    finally:
                        break
        else: # else
            self.display.setText(self.display.text() + key)

    def keyPressEvent(self, e): # https://freeprog.tistory.com/331
        def isPrintable(key): 
            printable = [ 
            Qt.Key_ParenLeft, # (
            Qt.Key_ParenRight, # )
            Qt.Key_Asterisk, # *
            Qt.Key_Plus, # +
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
            ]

            if key in printable: 
                return True 
            else:
                return False 
        
        control = False 

        if e.modifiers() & Qt.ControlModifier:
            control = True
        if e.modifiers() & Qt.ShiftModifier:
            pass
        if e.modifiers() & Qt.AltModifier:
            pass
        # elif e.key() == Qt.Key_Backspace: # backspace # 원본 코드를 실행했을 때는 잘 입력되는데 왜 안되는거지...
        #     self.display.setText(self.display.text()[:-1])
        elif e.key() in [Qt.Key_Return, Qt.Key_Enter]: # enter & eval -> evaluation
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error'
            self.display.setText(result)
        elif e.key() == Qt.Key_Escape: # esc -> clear
            self.display.setText('')

        if not control and isPrintable(e.key()):
            self.display.setText(self.display.text() + e.text())

    def clear_text(self):
        button = self.sender()
        key = button.text()

        if self.display.text() in ['Error', 'Div 0 Error', 'TypeError', 'ValueError']:
            self.display.setText('')
        
        if (self.display.text().startswith('0')) and (not self.display.text().startswith('0.')) and (key.isnumeric() or key in constantList): # 0123 -> 123
            self.display.setText('')

    
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())