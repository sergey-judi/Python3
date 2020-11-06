with open('input_task_05.txt', mode='r', encoding='utf8') as fin:
    maxNumber = int(fin.readline())
    numSet = set(range(1, maxNumber + 1))
    for numLine in fin:
        numLine = numLine.split()
        if numLine[0] != 'HELP':
            tempSet = set(numLine)
            yesOrNo = fin.readline().replace('\n', '')
            if yesOrNo == 'YES':
                numSet = tempSet
            else:
                numSet.difference_update(tempSet)
with open('output_task_05.txt', mode='w', encoding='utf8') as fout:
    print(*sorted(numSet), file=fout)


# max_num = int(input())
# avg_set = set([x for x in range(1, max_num + 1)])
# beat_set = input()
# b = set()
# while beat_set != 'HELP':
#     answer = str(input())
#     if answer == 'YES':
#         beat_set = set(map(int, beat_set.split()))
#         avg_set &= beat_set
#     elif answer == 'NO':
#         beat_set = set(map(int, beat_set.split()))
#         b |= beat_set
#     beat_set = input()
# print(*sorted(list(avg_set - b)))