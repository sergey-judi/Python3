n = int(input())
maxCount = 1
curCount = 1
while n != 0:
    nprev = n
    n = int(input())
    if n == nprev:
        curCount += 1
        if curCount > maxCount:
            maxCount = curCount
    else:
        curCount = 1
print(maxCount)
