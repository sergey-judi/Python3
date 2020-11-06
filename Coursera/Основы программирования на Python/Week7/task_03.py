numList = list(map(int, input().split()))
numSet = set()
for num in numList:
    if num in numSet:
        print('YES')
    else:
        numSet.add(num)
        print('NO')
