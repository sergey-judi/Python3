num = int(input())
if num < 10:
    print(0)
else:
    num = num % 100
    print((num - num % 10) // 10)
