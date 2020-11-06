p, x, y = int(input()), int(input()), int(input())
sum = x * 100 + y
sum += sum * p // 100
print(sum // 100, sum % 100)
