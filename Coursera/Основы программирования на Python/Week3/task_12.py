Str = input()
index = Str.find('f')
secondIndex = Str.find('f', index + 1)
if secondIndex == -1 and index != -1:
    print(-1)
elif index == -1:
    print(-2)
else:
    print(secondIndex)
