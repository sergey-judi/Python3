Str = input()
wordsAmount = 1
spacePos = Str.find(' ')
while spacePos != -1:
    if spacePos != len(Str) - 1:
        wordsAmount += 1
    spacePos = Str.find(' ', spacePos + 1)
print(wordsAmount)
