import time

#반복적으로 구현한 피보나치 수
def iterfibo(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    c = 0
    while c < n:
        a, b = b, a+b
        c += 1
    return a

#재귀적으로 구현한 피보나치 수열
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
