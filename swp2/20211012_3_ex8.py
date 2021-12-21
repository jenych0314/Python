import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        ok_button = QPushButton('OK')
        cancel_button = QPushButton('CANCEL')

        ok_button.clicked.connect(self.buttonClicked)
        cancel_button.clicked.connect(self.buttonClicked)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)
        # hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(vbox)
        self.show()
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(...)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())