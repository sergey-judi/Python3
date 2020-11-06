"""def createList(myList):
    listToReturn = []
    for record in myList:
        temp = record.split()
        listToReturn.append(temp)
    return listToReturn


def gradeSort(myList):
    return sum(map(int, myList[-3:]))


def removeGradeUnder40(myList):
    listToReturn = []
    for record in myList:
        temp = list(map(int, record[-3:]))
        if (temp[0] > 40 and
                temp[1] > 40 and
                temp[2] > 40):
            listToReturn.append(record)
    return listToReturn


def main():
    with open('input.txt', 'r', encoding='utf8') as fin:
        budjetNum = int(fin.readline())
        studentList = []
        for line in fin:
            studentList.append(line)
        myList = createList(studentList)
        myList.sort(reverse=True, key=gradeSort)
        myList = removeGradeUnder40(myList)
    with open('output.txt', 'w', encoding='utf8') as fout:
        if len(myList) < budjetNum:
            print(0, file=fout)
        elif len(myList) == budjetNum:
            print(1, file=fout)
        else:
            countedList = [0] * 301
            for record in myList:
                ind = sum(list(map(int, record[-3:])))
                countedList[ind] += 1
            lastMinGrade = 0
            k = 0
            for i in range(len(countedList) - 1, -1, -1):
                if countedList[i] + k <= budjetNum and countedList[i] != 0:
                    lastMinGrade = i
                    k += countedList[i]
            k = budjetNum
            for i in range(len(countedList) - 1, -1, -1):
                if k - countedList[i] >= 0 and countedList[i] != 0:
                    lastMinGrade = i
                    k -= countedList[i]
            print(lastMinGrade, file=fout)


main()"""

winner = open('output.txt', 'w', encoding='utf8')
students = open('input.txt', 'r', encoding='utf8')
more_40 = []
for line in students:
    line = line.split()
    if len(line) == 1:
        k = int(line[0])
    elif int(line[-1]) >= 40 and int(line[-2]) >= 40 and int(line[-3]) >= 40:
        b = int(line[-1]) + int(line[-2]) + int(line[-3])
        more_40.append(b)
more_40.sort(key=lambda p: -p)
ans = 1
if len(more_40) > k:
    for now in more_40:
        if now > more_40[k]:
            ans = now
    print(ans, file=winner)
elif len(more_40) <= k:
    print('0', file=winner)