# [20181592 김재민] 보고서

주석에 친절하게 설명이 나와있어서 과제 전 걱정했던 것보단 좀 더 수월하게 과제 수행을 하였습니다. 전 과제에서 아스키 코드표를 사용하여 예외처리를 했던 제 코드를 사용하여 마찬가지로 똑같이 예외처리를 하였습니다. 이때 교수님께서 좀 더 이해하기 쉽고 보기좋게 코드표 숫자 65와 90을 각각 ord("A")와 ord("Z")로 바꾸면 좋겠다고 하셨고, 더 이해하기 쉽고 보기좋은 방법으로 upper와 lower를 말씀해주셨습니다. 앞의 방법보단 뒤의 방법이 더 낫기 때문에 기존의 코드(주석처리된 코드)를 뒤의 방법을 사용한 코드(주석처리가 안된 코드)로 수정하였습니다.
#if 65 <= ord(guessedChar) <= 90:
#    guessedChar = chr(ord(guessedChar) + 32)
if guessedChar.upper():
     guessedChar = guessedChar.lower()

그리고 저는 단어의 길이를 애초에 제한해버리는 방식을 통해 단어를 보여주는 창의 크기를 조정할 필요가 없도록 했었습니다. 하지만 한 조원분께서 아래와 같은 코드를 작성하여 단어를 보여주는 창의 크기를 조절하는 코드를 작성하였습니다.
self.currentWord.setFixedWidth(self.font.pointSize()*len(self.guess.secretWord))
단어의 길이에 따라 창의 길이가 그에 맞춰 변하기 때문에 단어가 짤리는 문제가 발생하지않습니다. 위 코드 맨뒤에 숫자를 더하여 창의 길이를 늘려 단어가 아무리 길어져도 창은 고정되도록 시도해봤지만 아무리 큰 숫자를 더하여 창의 길이를 늘려도 길이가 16보다 긴 단어들이 나오면 무조건 창의 길이가 기존보다 더 늘어났습니다.
