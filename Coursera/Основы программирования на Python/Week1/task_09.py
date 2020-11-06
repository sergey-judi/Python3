number = int(input())
numSum = 0
for i in range(3):
    numSum += number % 10
    number = (number - number % 10) // 10
print(numSum)
