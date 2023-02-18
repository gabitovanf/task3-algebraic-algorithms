import sys
import time

sys.path.append('./tester')

from TestingInstanceInterface import TestingInstanceInterface, compareFloat, getNumDigits

class FibonacciTestingAdapter(TestingInstanceInterface):
    def __init__(self, function):
        self.function = function

    def compute(self, *input) -> str:
        print('Start with', input)

        try:
            firstInputVal = input[0]
            firstInputVal = int(firstInputVal)
            computed = self.function(firstInputVal)
        except ValueError as e:
            computed = 'Invalid input data'
            print(e)

        except Exception as e:
            code = e.__class__.__name__
            computed = f"Exception occured: {code} {e}"
            print(e)

        print('End with', computed)
        
        return str(computed)

    def validate(self, *input, output:str = '') -> dict:
        starttime = time.time()
        computed = self.compute(*input)
        secondsPassed = time.time() - starttime

        inputList = list(map(lambda x: int(x), input))
        input0 = None
        if len(inputList) > 0: input0 = inputList[0]

        return ({ 
            "valid": computed == output, 
            "computed": computed, 
            "expected": output, 
            "seconds": secondsPassed,
            "input": input0
        })

    def getEntityName(self) -> str:
        return self.function.__qualname__

        