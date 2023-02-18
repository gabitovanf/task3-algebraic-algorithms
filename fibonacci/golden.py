import sys
import math

sys.path.append('./power-computation')

from PowerBinaryDecomposition import powerBinaryDecomposition

sqrt5 = math.sqrt(5)
fert = (1 + sqrt5) / 2

def FibonacciGoldenRatioFormula(num:int) -> int:
    # if num == 0: return 0
    return int(math.trunc(pow(fert, num) / sqrt5 + 0.5))
    # return int(math.trunc(powerBinaryDecomposition(fert, num + 1) / sqrt5 + 0.5))
