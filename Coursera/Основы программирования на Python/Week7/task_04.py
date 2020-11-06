with open('input.txt', mode='r', encoding='utf8') as fin:
    wordSet = set()
    for line in fin:
        tempSet = line.split()
        for word in tempSet:
            wordSet.add(word)
with open('output.txt', mode='w', encoding='utf8') as fout:
    fout.write(str(len(wordSet)))
