import time
import random

#선형 탐색 알고리즘
def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

#이진 탐색의 재귀적 구현
def recbinsearch(L, l, u, target):
    l = 0
    u = len(L) - 1
    return -1

    while (l <= u):
        m = int((l + u) // 2)
        if L[m] == target :
            idx = m
            break
        elif L[m] < target :
            recbinsearch(L, m + 1, u, target)
        else:
            recbinsearch(L, l, m - 1, target)
    return idx

numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]

ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
