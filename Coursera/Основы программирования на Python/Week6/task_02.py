length = int(input())
numList = list(map(int, input().split()))
numList.sort()
print(*numList)
