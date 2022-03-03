import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        lcd = QLCDNumber()
        slider = QSlider(Qt.Orientation.Horizontal)

        slider.valueChanged.connect(lcd.display)
        layout = QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)

        self.setGeometry(500, 500, 500, 500) # (x, y, m, n) (x,y)에 m*n 크기로 만들겠다
        self.setWindowTitle('Review')
        self.show()
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())