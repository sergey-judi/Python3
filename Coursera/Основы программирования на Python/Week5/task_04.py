def printStair(n):
    stair = ''
    for i in range(n):
        stair += str(i + 1)
        print(stair)


def main():
    n = int(input())
    printStair(n)


main()
