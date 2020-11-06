numList = list(map(int, input().split()))
minimum = 1000
for num in numList:
    if 0 < num < minimum:
        minimum = num
print(minimum)
