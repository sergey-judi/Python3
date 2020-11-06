list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
i = 0
j = 0
newList = []
while i != len(list1) and j != len(list2):
    if list1[i] <= list2[j]:
        newList.append(list1[i])
        i += 1
    else:  # elif list2[j] < list1[i]:
        newList.append(list2[j])
        j += 1
else:
    if i == len(list1):
        for k in range(j, len(list2)):
            newList.append(list2[k])
    else:  # elif j == len(list2):
        for k in range(i, len(list1)):
            newList.append(list1[k])
print(' '.join(map(str, newList)))
