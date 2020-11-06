numList = list(map(int, input().split()))
maximum = -1
index = 0
for i in range(len(numList)):
    if numList[i] >= maximum:
        maximum = numList[i]
        index = i
print(maximum, index)
