mylist = []
n = int(input())
while n != 0:
    mylist.append(n)
    n = int(input())
print(sum(mylist, 0))
