def MinDivisor(n) -> int:
    i = 2
    while n % i != 0:
        i += 1
        if i > n**0.5:
            return n
    return i


def main() -> None:
    number = int(input())
    print(MinDivisor(number))


main()
