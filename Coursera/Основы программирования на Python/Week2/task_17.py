mylist = []
n = int(input())
i = 1
while i != n + 1:
    mylist.append(i ** 2)
    i += 1
print(sum(mylist, 0))
