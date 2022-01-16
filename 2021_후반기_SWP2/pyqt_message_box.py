import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.left = 100
        self.top = 100

        self.width = 320
        self.height = 200

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('MessageBox')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def closeEvent(self, event):
        button_title = 'Close Message'
        button_message = f"Do you want to close?"
        buttonReply = QMessageBox.question(self, button_title, button_message, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if buttonReply == QMessageBox.Yes:
            print('yes')
            event.accept()
        # if buttonReply == QMessageBox.No:
        #     print('no')
        # if buttonReply == QMessageBox.Cancel:
        #     print('cancel')
        else:
            event.ignore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())