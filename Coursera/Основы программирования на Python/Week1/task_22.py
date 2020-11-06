def decideIfSymmetric(_number: str):
    for i in range(4):
        if not _number[i] == _number[3 - i]:
            return -1
    return 1


def mainFunc():
    number = input()
    if len(number) == 3:
        number = '0' + number
    return decideIfSymmetric(number)


print(mainFunc())
