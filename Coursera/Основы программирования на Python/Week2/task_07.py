cows = int(input())
lastDigit = cows % 10
if 10 < cows < 20 \
        or lastDigit == 0 \
        or lastDigit == 5 \
        or lastDigit == 6 \
        or lastDigit == 7 \
        or lastDigit == 8 \
        or lastDigit == 9:
    print(cows, 'korov')
elif lastDigit == 1:
    print(cows, 'korova')
else:
    print(cows, 'korovy')
