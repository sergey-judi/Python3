Str = input()
spaceIndex = Str.find(' ')
newStr = Str[spaceIndex + 1:] + ' ' + Str[:spaceIndex]
print(newStr)
