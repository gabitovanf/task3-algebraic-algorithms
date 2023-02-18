import sys

sys.path.append('./tester')
sys.path.append('./prime-search')

from Tester import Tester
from PrimeDivisorsEnumeration import PrimeDivisorsEnumeration
from PrimesTestingAdapter import PrimesTestingAdapter

reportTrueDetails = """
    ----
    Целое число N: {input}
    Количество простых чисел от 1 до N: {computed}
    ----
"""

reportFalseDetails = """
    ----
    Целое число N: {input}

    Количество простых чисел от 1 до N
    - ожидаемое: {expected}
    - расчетное: {computed}
    ----
"""

tester0 = Tester(PrimesTestingAdapter(PrimeDivisorsEnumeration()))

tester0.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)

tester0.testdir('./tests/5.Primes', './report/5.Primes.report.divisorsEnumeration.01.txt')

