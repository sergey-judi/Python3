def min4(a, b, c, d):
    return min(min(a, b), min(c, d))


def main():
    a, b = int(input()), int(input())
    c, d = int(input()), int(input())
    print(min4(a, b, c, d))


main()
