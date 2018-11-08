class Guess:
    #game.py에서 guess를 정의하면서 Guess 클래스에 던진 단어 하나를 "word"로 받았음
    def __init__(self, word):
        #랜덤으로 받은 단어를 저장(이하 변수들은 game.py에 미리 쓰여있던 변수 이름들을 그대로 가져온 것)
        self.secretWord = word
        #입력했던 문자들을 저장하는 리스트
        self.guessedChars = []
        #실패한 횟수
        self.numTries = 0
        #맞추기전 초기상태
        self.currentStatus = list('_'*len(word))
        #맞추기전 초기상태의 또다른 코드
        #self.currentStatus = []
        #for i in range(len(word)):
        #    self.currentStatus.append('_')
        self.guessedChars2 = []

    def display(self):
        print('Current : ' + ''.join(self.currentStatus))
        print("Tries : " , self.numTries)
    #guessedChar 즉, 입력된 문자를 character로 받음
    def guess(self, character):
        #입력한 문자를 저장
        self.guessedChars.append(character)
        #입력한 문자가 단어에 있으면
        if character in self.secretWord:
            #단어에서 입력한 문자의 자리를 찾아 "_"를 입력한 문자로 변경
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus[i] = character
        #입력한 문자가 단어에 없다면
        else:
            #실패한 횟수를 1회 추가
            self.numTries += 1
        #랜덤으로 받은 단어를 완벽하게 찾았다면
        if self.secretWord == ''.join(self.currentStatus):
            return True
        #완벽하게 단어를 찾지 못했다면
        #초기 값이 False였기 때문에 이 else문은 없어도 되긴함
        else:
            return False