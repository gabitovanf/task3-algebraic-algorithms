import sys
import time

sys.path.append('./tester')

from TestingInstanceInterface import TestingInstanceInterface, compareFloat, getNumDigits

class PowerFunctionTestingAdapter(TestingInstanceInterface):
    def __init__(self, function, deviation = None):
        self.function = function
        self.deviation = deviation

    def compute(self, *input) -> str:
        print('Start with', input)

        try:
            inputFloat = tuple(map(lambda val: float(val) ,input))
            print(inputFloat)
            inputFloat = inputFloat[0:2]
            computed = self.function(*inputFloat)
        except ValueError as e:
            computed = 'Invalid input data'
            print(e)

        except Exception as e:
            computed = 'Unknown exception occured'
            print(e)

        print('End with', computed)
        
        return computed

    def validate(self, *input, output:str = '') -> dict:
        starttime = time.time()
        computed = self.compute(*input)
        secondsPassed = time.time() - starttime

        return ({
            "valid": compareFloat(computed=computed, output=output, deviation=self.deviation),
            "computed": computed,
            "expected": output, 
            "deviation": self.deviation, 
            "difference": computed - float(output), 
            "seconds": secondsPassed, 
            "input": list(input)
            })

    def getEntityName(self) -> str:
        return self.function.__qualname__

        