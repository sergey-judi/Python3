def IsPrime(n) -> bool:
    minDivisor = MinDivisor(n)
    return True if minDivisor == n else False


def MinDivisor(n) -> int:
    i = 2
    while n % i != 0:
        i += 1
        if i > n**0.5:
            return n
    return i


def main() -> None:
    number = int(input())
    print('YES') if IsPrime(number) else print('NO')


main()
