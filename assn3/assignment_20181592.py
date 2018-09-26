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

        self.btn1.clicked.connect(self.addDB)
        self.btn2.clicked.connect(self.delDB)
        self.btn3.clicked.connect(self.findDB)
        self.btn4.clicked.connect(self.incDB)
        self.btn5.clicked.connect(self.showScoreDB)

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
        # self.results = ""
        self.resultEdit.clear()
        self.results = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.keys]):
            for attr in sorted(p):
                self.results += str(attr) + "=" + str(p[attr]) + str("      ")
            self.results += "\n"
        self.resultEdit.setText(self.results)
        self.results = ""

    def addDB(self):
        try:
            int(self.ageEdit.text()) and int(self.scoreEdit.text())

        except:
            self.resultEdit.setText("Please Input Integer to Age or Score!")

        else:
            record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoreEdit.text()}
            self.scoredb += [record]
            self.showScoreDB()

    def delDB(self):
        self.delcount = 0
        for i in self.scoredb[::-1]:

            if i['Name'] == self.nameEdit.text():
                self.scoredb.remove(i)
                self.delcount = 1

        if self.delcount == 0:
            if self.nameEdit.text() == '':
                self.resultEdit.setText("Please input Name!")

            else:
                self.resultEdit.setText("He is Not in here!")
        else:
            self.showScoreDB()

    def findDB(self):
        self.findcount = 0
        self.resultEdit.clear()
        for i in self.scoredb:
            if i['Name'] == self.nameEdit.text():
                self.findcount = 0
                self.results += "Name = " + str(i['Name']) + " // " + "Age = " + str(
                    i['Age']) + " // " + "Score = " + str(i['Score'])
                self.results += "\n"
                self.resultEdit.setText(self.results)
                self.findcount = 1

            if self.findcount == 0:
                self.resultEdit.setText("He(She) is not in here!")

    def incDB(self):
        try:
            int(self.amountEdit.text())

        except:
            self.resultEdit.setText("Please Input Integer to Score!")

        else:
            self.k = 0
            for i in self.scoredb:
                if i['Name'] == self.nameEdit.text():
                    temp = int(i["Score"]) + int(self.amountEdit.text())
                    i["Score"] = str(temp)
                    self.k = 1

            if self.k == 0:
                self.resultEdit.setText("He is Not in here!")

            elif self.k == 1:
                self.showScoreDB()


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

