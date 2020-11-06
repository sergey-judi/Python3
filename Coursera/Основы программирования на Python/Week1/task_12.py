a = int(input())
b = int(input())
num = int(input())
value = a * 100 + b
value *= num
a = value // 100
b = value % 100
print(a, b)
