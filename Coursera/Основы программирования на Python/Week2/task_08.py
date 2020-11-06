def sgn(x: int):
    if x == 0:
        return 0
    else:
        return 1 if x > 0 else -1


print(sgn(int(input())))