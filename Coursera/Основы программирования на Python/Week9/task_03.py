from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() != other.size():
            raise MatrixError(self, other)
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

    def transpose(self):
        rows, cols = self.size()
        transposedMatrix = []
        newRow = []
        for j in range(cols):
            for i in range(rows):
                newRow.append(self.matrix[i][j])
            transposedMatrix.append(newRow)
            newRow = []
        self.matrix = transposedMatrix
        return Matrix(self.matrix)

    @staticmethod
    def transposed(matrixObj):
        rows, cols = matrixObj.size()
        transposedMatrix = []
        newRow = []
        for j in range(cols):
            for i in range(rows):
                newRow.append(matrixObj.matrix[i][j])
            transposedMatrix.append(newRow)
            newRow = []
        return Matrix(transposedMatrix)


exec(stdin.read())
