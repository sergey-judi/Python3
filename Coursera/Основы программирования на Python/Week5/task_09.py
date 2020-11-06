numList = list(map(int, input().split()))
for i in range(1, len(numList)):
    if numList[i] > numList[i - 1]:
        print(numList[i], end=' ')
