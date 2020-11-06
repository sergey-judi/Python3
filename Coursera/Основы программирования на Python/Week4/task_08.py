def power(a, n) -> float:
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * power(a, n - 1)


def main() -> None:
    a = float(input())
    n = float(input())
    print(power(a, n))


main()
