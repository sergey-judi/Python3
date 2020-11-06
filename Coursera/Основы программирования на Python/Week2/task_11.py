a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a <= d and (b <= e or c <= e):
    print('YES')
elif b <= d and (a <= e or c <= e):
    print('YES')
elif c <= d and (a <= e or b <= e):
    print('YES')
else:
    print('NO')
