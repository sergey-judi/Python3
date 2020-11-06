with open('input_task_07.txt', mode='r') as fin, \
        open('output_task_07.txt', mode='w') as fout:
    wordAppearance = {}
    for line in fin:
        wordList = line.split()
        for word in wordList:
            if word not in wordAppearance:
                wordAppearance[word] = 0
            else:
                wordAppearance[word] += 1
            print(wordAppearance[word], end=' ',  file=fout)
