def createList(myList):
    listToReturn = []
    for record in myList:
        temp = record.split()
        listToReturn.append(temp)
    return listToReturn


def gradeSort(listI):
    return [-int(listI[1]), listI[0]]


def getSurnames(myList):
    return [record[0] + '\n' for record in myList]


def main():
    with open('input_task_07.txt', 'r', encoding='utf8') as fin:
        recordsNum = fin.readline()
        studentList = []
        for line in fin:
            studentList.append(line)
        myList = createList(studentList)
        myList.sort(key=gradeSort)
        myList = getSurnames(myList)
    with open('output_task_07.txt', 'w', encoding='utf8') as fout:
        print(*myList, sep='', end='', file=fout)


main()
