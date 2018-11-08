from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    #guess 는 Guess 클래스에 랜덤으로 단어 하나를 인자로 던진 것
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    #목숨의 개수를 초기화
    maxTries = hangman.getLife()
    #실패한 횟수가 목숨보다 적으면 계속 실행
    while guess.numTries < maxTries:
        #display라는 변수를 통해 만들어서 행맨 모양을 불러옴
        display = hangman.get(maxTries - guess.numTries)
        #행맨 모양 출력
        print(display)
        #Current 와 Tries 출력
        guess.display()
        #입력한 문자를 guessedChar라고 함
        guessedChar = input('Select a letter: ')
        #입력한 문자가 한글자가 아니라면
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        #입력한 문자가 대문자라면
        if 65 <= ord(guessedChar) <= 90:
            #소문자로 변경
            guessedChar = chr(ord(guessedChar) + 32)
        #입력한 문자가 이미 입력했던 문자라면
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue
        #알파벳 이외의 다른 모든 경우의 수를 차단
        if ord(guessedChar) <= 64 or 91 <= ord(guessedChar) <= 96 or 123 <= ord(guessedChar):
            print('Please enter the alphabet!')
            continue
        #guess 모듈로 넘어가서 입력한 문자에 대해 처리
        finished = guess.guess(guessedChar)
        #단어가 완성되었을 때 while 탈출
        if finished == True:
            break

    if finished == True:
        print('Success')
    #단어가 완성되어서 탈출한게 아니라 목숨의 개수가 다달아서 False인 상태에서 while문을 빠져나온 경우
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + ''.join(guess.currentStatus) + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
