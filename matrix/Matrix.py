from Vector2 import Vector2
from MatrixInvalidException import MatrixInvalidException
from MatrixDimensionException import MatrixDimensionException
from MatrixInvalidParametersException import MatrixInvalidParametersException

class Matrix:

    validateFloat = True

    @staticmethod
    def __get_dimension(rowList:list):
        numRows = len(rowList)

        rowLengths = Matrix.__get_row_lengths(rowList)
        minRowLength = min(*rowLengths)

        # numRows by numCols
        # i.e. y by x
        return Vector2(minRowLength, numRows)

    @staticmethod
    def __create_dimension(cols:int, rows:int):
        # numRows by numCols
        # i.e. y by x
        return Vector2(cols, rows)

    @staticmethod
    def __create_empty_rowslist(cols:int, rows:int):
        return [[0]*cols for i in enumerate(list([1] * rows))]

    @staticmethod
    def __all_are_numbers(rowList:list) -> tuple:
        def allNumbers(valList) -> bool:
            return all(list(map(lambda x: isinstance(x, (float, int)), valList)))

        return all(list(map(lambda row: allNumbers(row), rowList)))

    @staticmethod
    def __get_row_lengths(rowList:list) -> tuple:
        return tuple(map(lambda row: len(row), rowList))

    @staticmethod
    def __clamp(rowList:list, maxNumCols:int) -> list:
        return list(map(lambda row: row[0:maxNumCols], rowList))

    @staticmethod
    def __clone(m) -> list:
        return Matrix(m.__rowList)

    def __init__(self, inputRowList = None, clamp:bool = True, cols:int = None, rows:int = None):
        if inputRowList != None:
            self.fromList(inputRowList, clamp)
        elif rows != None and cols != None:
            self.empty(cols, rows)
        else:
            raise MatrixInvalidParametersException

    def empty(self, cols:int, rows:int):
        dimension = Matrix.__create_dimension(cols, rows)

        self.__rowList = Matrix.__create_empty_rowslist(cols, rows)
        self.__valid = True
        self.__dimension = dimension

    @staticmethod
    def identity(cols:int, rows:int):
        rowsList = Matrix.__create_empty_rowslist(cols, rows)

        for rindex in range(0, rows):
            rowsList[rindex][rindex] = 1

        return Matrix(rowsList)

    def fromList(self, inputRowList, clamp:bool = True):
        rowList = list(inputRowList)
        dimension = Matrix.__get_dimension(rowList)
        equal = max(*Matrix.__get_row_lengths(rowList)) == dimension.x

        if clamp:
            rowList = Matrix.__clamp(rowList, dimension.x)
            equal = True

        self.__rowList = rowList
        self.__valid = Matrix.__all_are_numbers(rowList) and equal
        self.__dimension = dimension

    def isValid(self) -> bool:
        return self.__valid

    def get(self, xindex:int, yindex:int):
        return self.__rowList[yindex][xindex]

    def dimension(self):
        return self.__dimension

    def clone(self):
        return Matrix.__clone(self)

    def __str__(self) -> str:
        return "Matrix: {s} ({y} by {x})".format(s = str(self.__rowList), x = self.__dimension.x, y = self.__dimension.y)

    def __add__(self, m):
        if not self.__valid or not m.__valid:
            raise MatrixInvalidException
        elif not self.__dimension.equal(m.__dimension):
            raise MatrixDimensionException

        mRowsList = m.__rowList
        newRowsList = []

        for rindex, row in enumerate(self.__rowList):
            newRowsList.append([(val + mRowsList[rindex][cindex]) for cindex, val in enumerate(row)])

        return Matrix(newRowsList)

    def __sub__(self, m):
        if not self.__valid or not m.__valid:
            raise MatrixInvalidException
        elif not self.__dimension.equal(m.__dimension):
            raise MatrixDimensionException

        mRowsList = m.__rowList
        newRowsList = []

        for rindex, row in enumerate(self.__rowList):
            newRowsList.append([(val - mRowsList[rindex][cindex]) for cindex, val in enumerate(row)])

        return Matrix(newRowsList)

    def __mulScalar(self, m):
        newRowsList = []

        for rindex, row in enumerate(self.__rowList):
            newRowsList.append([(val * m) for cindex, val in enumerate(row)])

        return Matrix(newRowsList)

    def __mul__(self, m):
        if isinstance(m, (float, int)): return self.__mulScalar(m)

        if not self.__valid or not m.__valid:
            raise MatrixInvalidException
        elif not self.__dimension.x == m.__dimension.y:
            raise MatrixDimensionException

        mRowsList = m.__rowList
        newNumCols = m.__dimension.x
        newRowsList = []

        def computeRowValues(rindex, row):
            newRow = []
            for cindex in range(0, newNumCols):
                cellVal = sum([(val * mRowsList[valindex][cindex]) for valindex, val in enumerate(row)])
                newRow.append(cellVal)

            return newRow
                
        return Matrix([computeRowValues(rindex, row) for rindex, row in enumerate(self.__rowList)])

    def __pow__(self, num:int):
        if not self.__valid:
            raise MatrixInvalidException
        elif not self.__dimension.x == self.__dimension.y:
            raise MatrixDimensionException

        i = num
        curFactor = self.clone()
        result = Matrix.identity(*self.__dimension.tuple())

        if i % 2 > 0:
            result = result * curFactor

        while(i > 1):
            i //= 2
            curFactor = curFactor * curFactor
            if i % 2 > 0:
                result = result * curFactor

        return result
        

