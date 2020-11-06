curX = int(input())
curY = int(input())
anotherX = int(input())
anotherY = int(input())
if (curX * anotherX) % 2 == 0 and (curY * anotherY) % 2 == 0:
    print('YES')
else:
    print('NO')
