from copy import deepcopy
from sys import stdin


class Matrix:
    def __init__(self, listOfLists):
        self.matrix = deepcopy(listOfLists)

    def size(self):
        rowsAmount = len(self.matrix)
        colsAmount = len(self.matrix[0])
        return (rowsAmount, colsAmount)

    def __str__(self):
        strToReturn = []
        for row in self.matrix:
            strToReturn.append('\t'.join(map(str, row)))
        return '\n'.join(strToReturn)

    def __add__(self, other):
        result = []
        for i in range(self.size()[0]):
            result.append(
                list(
                    map(
                        lambda x, y: x+y,
                        self.matrix[i],
                        other.matrix[i]
                    )
                )
            )
        return Matrix(result)

    def __mul__(self, scalarValue):
        result = []
        for i in range(self.size()[0]):
            result.append(
                list(
                    map(
                        lambda x: x * scalarValue,
                        self.matrix[i]
                    )
                )
            )
        return Matrix(result)

    __rmul__ = __mul__


exec(stdin.read())
