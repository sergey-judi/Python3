numList = list(map(int, input().split()))
numGTZ = 0
for num in numList:
    if not num <= 0:
        numGTZ += 1
print(numGTZ)
