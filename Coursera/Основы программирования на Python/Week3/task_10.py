Str = input()
index = Str.find('f')
reversedIndex = Str[index + 1:].find('f')
if reversedIndex == -1 and index != -1:
    print(index)
elif reversedIndex != -1:
    reversedIndex = len(Str) - 1 - Str[::-1].find('f')
    print(index, reversedIndex)
