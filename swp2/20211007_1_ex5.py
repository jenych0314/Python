import sys
from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        title_label = QLabel('Title', self)
        author_label = QLabel('Author', self)
        review_label = QLabel('Review', self)
        title_eidt = QLineEdit()
        author_eidt = QLineEdit()
        review_edit = QTextEdit()

        widgets = [title_label, title_eidt,
                    author_label, author_eidt,
                    review_label, review_edit]

        positions = [(i, j) for i in range(3) for j in range(2)]

        for position, widget in zip(positions, widgets):
            grid.addWidget(widget, *position)
            if widget == 'review_edit':
                grid.addWidget(review_edit, 3, 1, 5, 1)

        grid.setSpacing(10)
        self.move(300, 150)        
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())