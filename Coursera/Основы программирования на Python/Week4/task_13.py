def ReversedSeries():
    n = int(input())
    if n != 0:
        ReversedSeries()
        print(n)
    else:
        print(n)


ReversedSeries()
