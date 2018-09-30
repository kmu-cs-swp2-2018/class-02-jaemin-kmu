import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItems(['Name', 'Age', 'Score'])
        self.resultEdit = QTextEdit()

        self.btn1 = QPushButton("Add")
        self.btn2 = QPushButton("Del")
        self.btn3 = QPushButton("Find")
        self.btn4 = QPushButton("Inc")
        self.btn5 = QPushButton("show")

        self.btn1.clicked.connect(self.addDB)
        self.btn2.clicked.connect(self.delDB)
        self.btn3.clicked.connect(self.findDB)
        self.btn4.clicked.connect(self.incDB)
        self.btn5.clicked.connect(self.showScoreDB)

        hbox = QHBoxLayout()
        hbox.addWidget(name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(score)
        hbox.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
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
        vbox.addWidget(result)
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
        keys = self.keyEdit.currentText()
        self.resultEdit.clear()
        self.results = ""
        for p in sorted(self.scoredb, key=lambda person: person[keys]):
            for attr in sorted(p):
                self.results += str(attr) + "=" + str(p[attr]) + str("    ")
            self.results += "\n"
        self.resultEdit.setText(self.results)

    def addDB(self):
        try:
            int(self.ageEdit.text()) and int(self.scoreEdit.text())

        except:
            self.resultEdit.setText("Please Input Integer to Age or Score!")

        else:
            if self.nameEdit.text() == '':
                self.resultEdit.setText("Please Input Name!")
            else:
                if int(self.ageEdit.text()) > 0 and int(self.scoreEdit.text()) > 0:
                    record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoreEdit.text()}
                    self.scoredb += [record]
                    self.showScoreDB()
                else:
                    self.resultEdit.setText("Please Input Positive Integer to Age or Score!")

    def delDB(self):
        self.delcount = 0
        for i in self.scoredb[::-1]:

            if i['Name'] == self.nameEdit.text():
                self.scoredb.remove(i)
                self.showScoreDB()
                self.delcount = 1

        if self.delcount == 0:
            if self.nameEdit.text() == '':
                self.resultEdit.setText("Please Input Name!")

            else:
                self.resultEdit.setText("He(She) is Not in here!")

    def findDB(self):
        self.results = ""
        self.findcount = 0
        for i in self.scoredb:
            if i['Name'] == self.nameEdit.text():
                self.results += "Age=" + str(i['Age']) + "    " + "Name=" + str(
                    i['Name']) + "    " + "Score=" + str(i['Score'])
                self.results += "\n"
                self.resultEdit.setText(self.results)
                self.findcount = 1

        if self.findcount == 0:
            if self.nameEdit.text() == '':
                self.resultEdit.setText("Please Input Name!")

            else:
                self.resultEdit.setText("He(She) is Not in here!")

    def incDB(self):
        try:
            int(self.amountEdit.text())

        except:
            self.resultEdit.setText("Please Input Integer to Score!")

        else:
            self.inccount = 0
            for i in self.scoredb:
                if i['Name'] == self.nameEdit.text():
                    updown = int(i["Score"]) + int(self.amountEdit.text())
                    i["Score"] = str(updown)
                    self.showScoreDB()
                    self.inccount = 1

            if self.inccount == 0:
                if self.nameEdit.text() == '':
                    self.resultEdit.setText("Please Input Name!")

                else:
                    self.resultEdit.setText("He(She) is Not in here!")

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

