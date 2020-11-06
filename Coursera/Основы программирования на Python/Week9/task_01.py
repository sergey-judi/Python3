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


exec(stdin.read())