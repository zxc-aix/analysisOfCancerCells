'''
with open('27-A.txt') as f:
    n = int(f.readline())
    s = list(map(int, f.readlines()))

k = 0
for i in range(n-1):
    element = s[i]
    for j in range(i+1, n):
        if (element * s[j]) % (10**7) == 0 and (element * s[j]) % (10**8) != 0:
            k+=1
print(k)

with open('27A.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    s = list(map(int, f.readlines()))

summ = 0
for i in range(n-25):
    for j in range(i+25, n):
        summ = max(summ, s[i] + s[j])
print(summ)

with open('27-140a.txt') as f:
    n = int(f.readline())
    s = list(map(int, f.readlines()))

k = 0
for x in range(n-34):
    for y in range(x+17, n-17):
        for z in range(y + 17, n):
            if (s[x] + s[y] + s[z]) % 7717 == 0:
                k += 1
print(k)        

import math
with open('27-123a.txt') as f:
    data = list(map(int, f.readline().split()))
    luk = []
    for i in range(data[0]):
        luk.append(list(map(int, f.readline().split())))
        
summ = 10**10
for i in range(data[0]):
    r = luk[i][0]
    res = 0 
    for j in range(data[0]):
        res += min(abs(luk[j][0] - r), abs(data[1] - luk[j][0] + r), abs(data[1] + luk[j][0] - r)) * math.ceil(luk[j][1] / data[2])
    summ = min(res, summ)
print(summ)

arr = []
for i in range(1, 1000):
    arr.append((i**2)/(2**i))
print(max(arr))

x1 = x2 = 1
print(x1, x2, end=' ')
for i in range(10):
    x2, x1 = x1 + x2, x2
    print(x2, end=' ')
'''
print
    
