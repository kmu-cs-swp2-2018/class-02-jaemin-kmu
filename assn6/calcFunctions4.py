from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    sum = 0
    attempt = False

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    for value, letters in romans:
        while numStr.find(letters) == 0:
            numStr = numStr[len(letters):]
            sum += value
            attempt = True

#출력창이 빈칸일때 버튼을 누르면 0이 출력되는 것을 Error!가 출력되게 하고
#출력창이 Error!일때 버튼을 누르면 0이 출력되는 것을 그대로 Error!가 출력되게 함.
        if numStr == '' and attempt == True:
            result = sum

        else:
            result = 'Error!'

    return result

