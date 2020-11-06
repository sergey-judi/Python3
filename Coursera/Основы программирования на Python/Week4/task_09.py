def sum(a, b) -> float:
    if a != 0:
        return 1 + sum(a - 1, b)
    elif b != 0:
        return 1 + sum(a, b - 1)
    else:
        return 0


def main() -> None:
    a = int(input())
    b = int(input())
    print(sum(a, b))


main()
