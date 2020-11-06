def main():
    x1, y1 = float(input()), float(input())
    x2, y2 = float(input()), float(input())
    x3, y3 = float(input()), float(input())
    side1 = calcDistance(x1, y1, x2, y2)
    side2 = calcDistance(x2, y2, x3, y3)
    side3 = calcDistance(x1, y1, x3, y3)
    perimeter = side1 + side2 + side3
    print(perimeter)


def calcDistance(x1, y1, x2, y2):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance


main()
