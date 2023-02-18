import sys

sys.path.append('./tester')
sys.path.append('./power-computation')

from Tester import Tester
from PowerIterate import powerIterate
from PowerIndian import powerIndian
from PowerBinaryDecomposition import powerBinaryDecomposition
from PowerFunctionTestingAdapter import PowerFunctionTestingAdapter

powerReportTrueDetails = """
    ----
    Число A и степень N: {input}
    Степень N числа A
    - ожидаемый результат: {expected}
    - расчетный результат: {computed}

    Погрешность: {deviation}
    Разница: {difference}
    ----
"""

powerReportFalseDetails = """
    ----
    Число A и степень N: {input}

    Степень N числа A
    - ожидаемый результат: {expected}
    - расчетный результат: {computed}
    ----
"""

testerPowerIterate = Tester(PowerFunctionTestingAdapter(powerIterate))
testerPowerIndian = Tester(PowerFunctionTestingAdapter(powerIndian, deviation = 0.00000003))
testerBinaryDecomposition = Tester(PowerFunctionTestingAdapter(powerBinaryDecomposition, deviation = 0.00000003))

testerPowerIterate.setupReportStrings(reportTrueDetails = powerReportTrueDetails, reportFalseDetails = powerReportFalseDetails)
testerPowerIndian.setupReportStrings(reportTrueDetails = powerReportTrueDetails, reportFalseDetails = powerReportFalseDetails)
testerBinaryDecomposition.setupReportStrings(reportTrueDetails = powerReportTrueDetails, reportFalseDetails = powerReportFalseDetails)


# testerPowerIterate.testdir('./tests/3.Power', './report/3.Power.report.powerIterate.01.txt')
# testerPowerIndian.testdir('./tests/3.Power', './report/3.Power.report.powerIndian.01.txt')
testerBinaryDecomposition.testdir('./tests/3.Power', './report/3.Power.report.powerBinaryDecomposition.01.txt')
