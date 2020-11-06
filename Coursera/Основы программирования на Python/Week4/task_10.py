def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * power(a, n - 1)
    else:
        return power(a**2, n // 2)


def main():
    a = float(input())
    n = int(input())
    print(power(a, n))


main()
