def SeriesSum():
    n = int(input())
    if n != 0:
        return n + SeriesSum()
    else:
        return 0

print(SeriesSum())
