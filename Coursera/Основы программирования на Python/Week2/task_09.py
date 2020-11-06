a, b, c = int(input()), int(input()), int(input())
mylist = [a, b, c]
for j in range(3):
    for i in range(2):
        if mylist[i] >= mylist[i + 1]:
            (mylist[i], mylist[i + 1]) = (mylist[i + 1], mylist[i])
for i in range(3):
    print(mylist[i], end=' ')
print()
