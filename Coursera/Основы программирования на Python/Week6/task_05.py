def createList(param4):
    listToReturn = []
    for record in param4:
        temp = record.split()
        listToReturn.append(' '.join([temp[0], temp[1], temp[3]]) + '\n')
    return listToReturn


def main():
    with open('input_task_05.txt', 'r', encoding='utf8') as fin:
        studentList = []
        for line in fin:
            studentList.append(line)
        myList = createList(studentList)
        myList.sort()
    with open('output_task_05.txt', 'w', encoding='utf8') as fout:
            print(*myList, sep='', end='', file=fout)


main()
