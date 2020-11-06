numList = list(map(int, input().split()))
minIndex = numList.index(min(numList))
maxIndex = numList.index(max(numList))
numList[minIndex], numList[maxIndex] = numList[maxIndex], numList[minIndex]
print(' '.join(map(str, numList)))
