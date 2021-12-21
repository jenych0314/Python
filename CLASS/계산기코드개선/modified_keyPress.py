from PyQt5.QtCore import Qt
from calcFunction import *

class keyPress:
    def keyPressEvent(self, e): # https://freeprog.tistory.com/331
        def isPrintable(key): 
            printable = [ 
            Qt.Key_Exclam, # !, factorial
            Qt.Key_Percent, # %, percent
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
            Qt.Key_Equal, # =, eval
            Qt.Key_AsciiCircum, # ^, pow
            ]

            if key in printable: 
                return True 
            else:
                return False 
        
        control = False 

        if e.key() == Qt.Key_Backspace: # back
            self.display.setText(self.display.text()[:-1])
        elif e.key() in [Qt.Key_Return, Qt.Key_Enter]: # enter & eval -> evaluation
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error'
            self.display.setText(result)
        elif e.key() == Qt.Key_Escape: # esc -> clear
            self.display.setText('')

        if not control and isPrintable(e.key()):
            if e.key() == Key_Exclam:
                try:
                    n = self.display.text()
                    value = calcFunction.factorial(n)
                    self.display.setText(str(value))
                except:
                    self.display.setText('Error')
            elif e.key() == Key_Percent:
                try:
                    n = self.display.text()
                    value = float(n) / 100
                    self.display.setText(str(value))
                except:
                    self.display.setText('Error')
            # elif e.key() == Key_AsciiCircum:
            #     try:
            #         n = self.display.text()
            #         value = float(n) / 100
            #         self.display.setText(str(value))
            #     except:
            #         self.display.setText('Error')
            self.display.setText(self.display.text() + e.text())