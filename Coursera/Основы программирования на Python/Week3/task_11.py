Str = input()
index = Str.find('h')
reversedIndex = len(Str) - 1 - Str[::-1].find('h')
print(Str[:index] + Str[reversedIndex + 1:])
