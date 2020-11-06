length = int(input())
numList = list(map(int, input().split()))
number = int(input())
absList = []
for num in numList:
    absList.append(abs(number - num))
minimum = min(absList)
minIndex = absList.index(minimum)
print(numList[minIndex])
