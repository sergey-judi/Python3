numList = list(map(int, input().split()))
listLength = len(numList)
for i in range(0, listLength - 1, 2):
    numList[i], numList[i + 1] = numList[i + 1], numList[i]
print(' '.join(map(str, numList)))
