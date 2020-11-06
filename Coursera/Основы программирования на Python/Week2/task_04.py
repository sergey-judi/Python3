curX = int(input())
curY = int(input())
moveX = int(input())
moveY = int(input())
if 0 <= abs(curX - moveX) <= 1 and 0 <= abs(curY - moveY) <= 1:
    print('YES')
else:
    print('NO')
