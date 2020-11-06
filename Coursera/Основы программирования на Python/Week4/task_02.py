def main():
    x1, y1 = float(input()), float(input())
    x2, y2 = float(input()), float(input())
    print(calcDistance(x1, y1, x2, y2))


def calcDistance(x1, y1, x2, y2):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance


main()
