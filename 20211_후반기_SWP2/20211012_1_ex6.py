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

        self.setGeometry(500, 500, 700, 800)    
        self.setWindowTitle('Review')
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())