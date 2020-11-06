spaceSize, usersAmount = tuple(map(int, input().split()))
myList = []
for i in range(usersAmount):
    userSize = int(input())
    myList.append(userSize)
myList.sort()
maxUsers = 0
spaceSum = 0
i = 0
while i != len(myList) and spaceSum + myList[i] <= spaceSize:
    spaceSum += myList[i]
    maxUsers += 1
    i += 1
print(maxUsers)
