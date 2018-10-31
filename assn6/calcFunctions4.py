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

#romans 리스트를 아예 밖에 따로 정의하여 두번 써야하는 반복을 피함.
romans = [
        (1000, 'M',4), (900, 'CM',2), (500, 'D',2), (400, 'CD',2),
         (100, 'C',4),  (90, 'XC',2),  (50, 'L',2),  (40, 'XL',2),
          (10, 'X',4),   (9, 'IX',2),   (5, 'V',2),   (4, 'IV',2),
           (1, 'I',4)
    ]
a = ['CM', 'D', 'CD']
b = ['XC', 'L', 'XL']
d = ['IX', 'V', 'IV']

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'

    result = ''
    for value, letters, count in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(n):
    #sum = 0
    #attempt = False

    #for value, letters, count in romans:
        #while n.find(letters) == 0:  # n.startswith(letters)
            #n = n[len(letters):]
            #sum += value
            #attempt = True

        # 출력창이 빈칸일때 버튼을 누르면 0이 출력되는 것을 Error!가 출력되게 하고
        # 출력창이 Error!일때 버튼을 누르면 0이 출력되는 것을 그대로 Error!가 출력되게 함.
        #if n == '' and attempt == True:
            #result = sum

        #else:
            #result = 'Error!'

    #return result

    result = 0
    attempt = False
    for value, letters, count in romans:
        cnt = 1
        while n.startswith(letters):
            flag = 0

            if letters in a:
                c = n.partition(letters)[2]
                if c in a:
                    break
                else:
                    flag = 1
            elif letters in b:
                c = n.partition(letters)[2]
                if c in b:
                    break
                else:
                    flag = 1
            elif letters in d:
                c = n.partition(letters)[2]
                if c in d:
                    break
                else:
                    flag = 1
            else:
                flag = 1

            if flag == 1:
                if cnt < count:
                    result += value
                    n = n[len(letters):]
                    cnt += 1
                    attempt = True
                else:
                    break
            elif flag == 0:
                break

    if n == '' and attempt == True:
        return result
    else:
        return 'Error!'


#for experiment
if __name__ == '__main__':
    n = input("Roman : ")
    print(romanToDec(n))