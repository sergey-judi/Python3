def IsPointInCircle(x, y, xc, yc, r) -> bool:
    distanceToPoint = CalcDistance(x, y, xc, yc)
    return IsInCircle(distanceToPoint, r)


def CalcDistance(x1, y1, x2, y2) -> float:
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance


def IsInCircle(lineWidth, radius) -> bool:
    return True if lineWidth <= radius else False


def main() -> None:
    x, y = float(input()), float(input())
    xc, yc, r = float(input()), float(input()), float(input())
    if IsPointInCircle(x, y, xc, yc, r):
        print('YES')
    else:
        print('NO')


main()
