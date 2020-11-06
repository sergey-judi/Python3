from math import ceil, floor
number = float(input())
part = abs(int(100 * round(number - int(number), 6)))
if part < 50:
    print(floor(number))
else:
    print(ceil(number))
