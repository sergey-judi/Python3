mylist = []
num = int(input())
mylist.append(num)
while num != 0:
    num = int(input())
    if num != 0:
        mylist.append(num)
mylist.sort()
print(mylist.count(mylist[len(mylist) - 1]))
