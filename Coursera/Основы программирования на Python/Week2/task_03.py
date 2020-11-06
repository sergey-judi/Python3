year = int(input())
if not year % 100 == 0 and year % 4 == 0:
    print('YES')
elif year % 400 == 0:
    print('YES')
else:
    print('NO')
