with open('input_task_06.txt', 'r', encoding='utf8') as fin:
    numList = list(map(int, fin.readline().split()))
    countedList = [0] * 101
    for number in numList:
        countedList[number] += 1
with open('output_task_06.txt', 'w', encoding='utf8') as fout:
    for i in range(len(countedList)):
        if countedList[i] != 0:
            print((str(i) + ' ') * countedList[i], sep='', end='', file=fout)
