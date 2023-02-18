import sys

sys.path.append('./tester')
sys.path.append('./fibonacci')
sys.path.append('./matrix')
sys.path.append('./power-computation')

from Tester import Tester
from recursion import FibonacciRecursion
from iteration import FibonacciIteration
from golden import FibonacciGoldenRatioFormula
from TransitionMatrixFibonacci import TransitionMatrixFibonacci
from FibonacciTestingAdapter import FibonacciTestingAdapter
from Matrix import Matrix

from PowerBinaryDecomposition import powerBinaryDecomposition

#
# print('Recursion limit:', sys.getrecursionlimit())
## 50000 is a maximum limit in my system (macOS)
# sys.setrecursionlimit(50000)
# print('Recursion limit:', sys.getrecursionlimit())
#

reportTrueDetails = """
    ----
    Номер числа Фибоначчи N: {input}
    N-ое число Фибоначчи: {computed}
    ----
"""

reportFalseDetails = """
    ----
    Номер числа Фибоначчи N: {input}

    N-ое число Фибоначчи
    - ожидаемое: {expected}
    - расчетное: {computed}
    ----
"""

tester0 = Tester(FibonacciTestingAdapter(FibonacciRecursion))
tester1 = Tester(FibonacciTestingAdapter(FibonacciIteration))
tester2 = Tester(FibonacciTestingAdapter(FibonacciGoldenRatioFormula))
tester3 = Tester(FibonacciTestingAdapter(TransitionMatrixFibonacci))

tester0.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester1.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester2.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester3.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)

tester0.testdir('./tests/4.Fibo', './report/4.Fibo.report.recursion.01.txt')
# tester1.testdir('./tests/4.Fibo', './report/4.Fibo.report.iteration.01.txt')
# tester2.testdir('./tests/4.Fibo', './report/4.Fibo.report.goldenRatioFormula.01.txt')
# tester3.testdir('./tests/4.Fibo', './report/4.Fibo.report.matrixPower.01.txt')
# tester3.testdir('./tests/temp', './report/TEMP.report.matrixPower.01.txt')


# print(sys.float_info)
# print(sys.int_info, pow(2, 30) * 4)


