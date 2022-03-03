import pickle
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QMessageBox)

class DB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.data_base = []
        self.keyname = 'Name'
        self.read_db()
        self.show_db(self.keyname)

    def initUI(self):
        labels = ('Name:', 'Age:', 'Score:', 'Amount:', 'Key:', 'Result:')
        commands = ('Add', 'Del', 'Find', 'Inc', 'Show')
        
        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.score_edit = QLineEdit()
        self.amount_edit = QLineEdit()

        self.key_edit = QComboBox()
        for i in range(3):
            self.key_edit.addItem(labels[i][:-1])
        self.keyname = self.key_edit.activated[str]
        self.key_edit.activated[str].connect(self.show_db)

        self.result_edit = QTextEdit()

        edits = (self.name_edit, self.age_edit, self.score_edit, self.amount_edit, self.key_edit, self.result_edit)
        
        hboxes = [QHBoxLayout() for i in range(5)]
        vbox = QVBoxLayout()

        for i in range(3): # name, age, score
            label = QLabel(labels[i])
            hboxes[0].addWidget(label)
            hboxes[0].addWidget(edits[i])

        hboxes[1].addStretch(1)
        for i in range(3, 5): # amount, key
            label = QLabel(labels[i])
            hboxes[1].addWidget(label)
            hboxes[1].addWidget(edits[i])
        
        hboxes[2].addStretch(1)

        self.add_button = QPushButton(commands[0]) # add
        self.add_button.clicked.connect(self.button_clicked)
        hboxes[2].addWidget(self.add_button)

        self.del_button = QPushButton(commands[1]) # del
        self.del_button.clicked.connect(self.button_clicked)
        hboxes[2].addWidget(self.del_button)

        self.find_button = QPushButton(commands[2]) # find
        self.find_button.clicked.connect(self.button_clicked)
        hboxes[2].addWidget(self.find_button)

        self.inc_button = QPushButton(commands[3]) # inc
        self.inc_button.clicked.connect(self.button_clicked)
        hboxes[2].addWidget(self.inc_button)

        self.show_button = QPushButton(commands[4]) # show
        self.show_button.clicked.connect(self.button_clicked)
        hboxes[2].addWidget(self.show_button)

        label = QLabel(labels[-1]) # result
        hboxes[3].addWidget(label)

        hboxes[4].addWidget(edits[-1])

        for i in range(5):
            vbox.addLayout(hboxes[i])
        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def closeEvent(self, event):
        self.write_db()

    def delEvent(self, name):
        button_title = 'Delete Message'
        button_message = f"Do you want to delete {name}?"
        buttonReply = QMessageBox.question(self, button_title, button_message, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if buttonReply == QMessageBox.Yes:
            return True
        else:
            return False

    def button_clicked(self):
        # button2func = {
        #     self.add_button: self.add_db(), 
        #     self.del_button: self.del_db(),
        #     self.find_button: self.find_db(),
        #     self.inc_button: self.inc_db(),
        #     self.show_button: self.show_db(self.keyname)}
        # for button in button2func.keys():
        #     print(button)
        #     if self.sender() == button:
        #         print('if')
        #         button2func[button]
        if self.sender() == self.add_button:
            self.add_db()
        elif self.sender() == self.del_button:
            self.del_db()
        elif self.sender() == self.find_button:
            self.find_db()
        elif self.sender() == self.inc_button:
            self.inc_db()
        elif self.sender() == self.show_button:
            self.show_db(self.keyname) 

    def read_db(self):
        try:
            fH = open(self.dbfilename, 'rb')
            self.data_base = pickle.load(fH)

            for data in self.data_base:
                data['Age'] = int(data['Age'])
                data['Score'] = int(data['Score'])
                
            fH.close()
        except FileNotFoundError:
            self.result_edit.setText('File not found')
            print('File not found')
            self.data_base = []
        except UnicodeDecodeError:
            self.result_edit.setText('File cannot decode')
            print('File cannot decode')
            self.data_base = []
        except UnicodeEncodeError:
            self.result_edit.setText('File cannot encode')
            print('File cannot encode')
            self.data_base = []
        return self.data_base

    def write_db(self):
        with open(self.dbfilename, 'wb') as fH:
            pickle.dump(self.data_base, fH)

    def show_db(self, keyname):

        self.keyname = keyname
        text = ''

        for personal_data in sorted(self.data_base, key = lambda person: person[self.keyname]):
            for attr in sorted(personal_data):
                text += attr + ' = ' + str(personal_data[attr]) + ' \t'
            text += '\n'

        self.result_edit.setText(text)

    def find_db(self):
        print('find')

        name = self.name_edit.text().strip()

        try:
            name = name[0].upper() + name[1:].lower()
            cnt = 0
            text = ''

            for personal_data in self.data_base:
                if personal_data['Name'] == name:
                    for attr in sorted(personal_data):
                        text += attr + ' = ' + str(personal_data[attr]) + ' \t'
                    text += '\n'
                    cnt += 1

            if cnt == 0:
                text = 'Cannot find ' + name
            
            self.result_edit.setText(text)
        except IndexError:
            self.result_edit.setText('Enter the name')
            print('IndexError')

    def inc_db(self):
        print('increase')

        name = self.name_edit.text().strip()
        amount = self.amount_edit.text()

        try:
            name = name[0].upper() + name[1:].lower()
            amount = int(amount)

            for personal_data in self.data_base:
                if personal_data['Name'] == name:
                    personal_data['Score'] += amount

            self.show_db(self.keyname)
        except ValueError:
            self.result_edit.setText('Enter Name: string, Amount: integer')
            print('Enter the amount integer')
        except IndexError:
            self.result_edit.setText('Enter the name and amount')
            print('IndexError')

    def add_db(self): 
        print('add')

        name = self.name_edit.text().strip()
        age = self.age_edit.text()
        score = self.score_edit.text()

        try:
            name = name[0].upper() + name[1:].lower()

            if not name.isalpha():
                raise ValueError

            record = {'Name':name, 'Age':int(age), 'Score':int(score)}
            self.data_base += [record]

            self.show_db(self.keyname)
        except ValueError:
            self.result_edit.setText('Enter the Name: string, Age: integer, Score: integer')
        except IndexError:
            self.result_edit.setText('Enter the Name, Age and Score.\nName can not be blankness')

    def del_db(self):
        print('del')

        name = self.name_edit.text().strip()

        try:
            name = name[0].upper() + name[1:].lower()

            if self.delEvent(name):
                for personal_data in sorted(self.data_base, key = lambda person: person['Name']):
                    if personal_data['Name'] == name:
                        self.data_base.remove(personal_data)

            self.show_db(self.keyname)
        except IndexError:
            self.result_edit.setText('Enter the name')
            print('IndexError')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = DB()
    sys.exit(app.exec_())