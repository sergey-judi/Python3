def IsPointInSquare(x, y) -> bool:
    return isInSquare(x, y)


def isInSquare(x, y) -> bool:
    return True if -1 <= x <= 1 and -1 <= y <= 1 else False


def main() -> None:
    x = float(input())
    y = float(input())
    if IsPointInSquare(x, y):
        print('YES')
    else:
        print('NO')


main()
