flat1 = int(input())
flat2 = int(input())
flatsAmount = flat2 - flat1 + 1
if (flat1 - 1) % flatsAmount == 0:
    print('YES')
else:
    print('NO')
