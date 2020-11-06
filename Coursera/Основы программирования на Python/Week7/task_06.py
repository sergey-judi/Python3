with open('input_task_06.txt', mode='r', encoding='utf8') as fin:
    pupilsNum = int(fin.readline())
    listOfSets = []
    for i in range(pupilsNum):
        languagesNum = int(fin.readline())
        tempSet = set()
        for j in range(languagesNum):
            curLang = ''.join(fin.readline().split())
            tempSet.add(curLang)
        listOfSets.append(tempSet)
    everyKnowsLang = listOfSets[0]
    atLeastOneKnows = listOfSets[0]
    for langSet in listOfSets:
        everyKnowsLang &= langSet
        atLeastOneKnows = atLeastOneKnows.union(langSet)
with open('output_task_06.txt', mode='w', encoding='utf8') as fout:
    print(len(everyKnowsLang), file=fout)
    print('\n'.join(list(everyKnowsLang)), file=fout)
    print(len(atLeastOneKnows), file=fout)
    print('\n'.join(list(atLeastOneKnows)), file=fout)
