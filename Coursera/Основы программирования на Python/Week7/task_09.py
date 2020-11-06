with open('input_task_09.txt', mode='r') as fin:
    wordDict = {}
    for line in fin:
        wordList = line.split()
        for word in wordList:
            if word not in wordDict:
                wordDict[word] = 0
            wordDict[word] += 1
with open('output_task_09.txt', mode='w') as fout:
    # print(sorted(wordDict, key=lambda x: (-wordDict[x], x))[0])
    print(max(sorted(wordDict), key=wordDict.get), file=fout)
