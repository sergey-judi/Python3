with open('input_task_08.txt', mode='r') as fin:
    pairs = int(fin.readline())
    wordDict = {}
    for i in range(pairs):
        pair = fin.readline().split()
        wordDict[pair[-1]] = pair[0]
        wordDict[pair[0]] = pair[-1]
    synonym = fin.readline().strip()
with open('output_task_08.txt', mode='w') as fout:
    print(wordDict[synonym], file=fout)
