from math import gcd


def ReduceFraction(n, m):
    divisor = gcd(n, m)
    n //= divisor
    m //= divisor
    return n, m


def main():
    n = int(input())
    m = int(input())
    print(*ReduceFraction(n, m))


main()
