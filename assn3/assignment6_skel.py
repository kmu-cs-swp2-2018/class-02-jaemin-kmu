import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.keys = "Name"
        self.results = ""

        self.name = QLabel('Name:', self)
        self.age = QLabel('Age:', self)
        self.score = QLabel('Score:', self)
        self.amount = QLabel('Amount:', self)
        self.key = QLabel('Key:', self)
        self.result = QLabel('Result:', self)

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)
        self.keyEdit = QComboBox(self)
        self.keyEdit.addItems(['Name', 'Age', 'Score'])
        self.resultEdit = QTextEdit(self)

        self.btn1 = QPushButton("Add", self)
        self.btn2 = QPushButton("Del", self)
        self.btn3 = QPushButton("Find", self)
        self.btn4 = QPushButton("Inc", self)
        self.btn5 = QPushButton("show", self)

        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(self.age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(self.score)
        hbox.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(self.key)
        hbox2.addWidget(self.keyEdit)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.btn1)
        hbox3.addWidget(self.btn2)
        hbox3.addWidget(self.btn3)
        hbox3.addWidget(self.btn4)
        hbox3.addWidget(self.btn5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.result)
        vbox.addWidget(self.resultEdit)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        #self.results = ""
        for p in sorted(self.scoredb, key=lambda person:person[self.keys]):
            for attr in sorted(p):
                self.results += str(attr) + "=" + str(p[attr]) + "\t"
            self.results += "\n"
        self.resultEdit.setText(self.results)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

