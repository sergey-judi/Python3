def isEven(_num):
    """
    This function checks if the number is even
    """
    if _num % 2 == 0:
        return True
    else:
        return False


def mainFunction() -> None:
    """
    This function prints the next even value for the current number
    """
    num = int(input())
    if isEven(num):
        print(num + 2)
    else:
        print(num + 1)


mainFunction()
