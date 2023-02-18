import sys

sys.path.append('./matrix')

from Matrix import Matrix

def getFibonacciTransition():
    return Matrix([[1, 1], [1, 0]])

def TransitionMatrixFibonacci(num:int) -> int:

    if num == 0:
        return 0
    
    fiboM = getFibonacciTransition()
    fiboM = fiboM ** (num - 1)

    return fiboM.get(0, 0)