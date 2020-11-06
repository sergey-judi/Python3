with open('input_task_10.txt', mode='r') as fin:
    wordDict = {}
    for line in fin:
        wordList = line.split()
        for word in wordList:
            if word not in wordDict:
                wordDict[word] = 0
            wordDict[word] += 1
with open('output_task_10.txt', mode='w') as fout:
    # sortedWordList = sorted(wordDict, key=lambda x: (-wordDict[x], x))
    print('\n'.
          join(sorted(wordDict, key=lambda x: (-wordDict[x], x))),
          file=fout
          )
