import math

class PrimeDivisorsEnumerationOptimize:
    @staticmethod
    def isPrime(a:int) -> bool:
        if a == 1: return False
        if a == 2: return True
        if a % 2 < 1: return False

        max = int(round(math.sqrt(a)))

        for dividor in range(3, max + 1, 2):
            if a % dividor < 1: return False

        return True
        
    @staticmethod
    def isPrimeBaseOnPrimes(primes:list, a:int) -> bool:
        if a == 1: return False
        if a == 2: return True
        if a % 2 < 1: return False

        max = int(round(math.sqrt(a)))

        for i, prime in enumerate(primes):
            if prime > max: break
            if a % prime < 1: return False

        return True

    def __init__(self, baseOnPrimes = True):
        self.__baseOnPrimes = baseOnPrimes

    def getNumPrimes(self, maxN:int) -> int:
        if self.__baseOnPrimes:
            return self.__getNumPrimesBaseOnPrimes(maxN)

        return self.__getNumPrimes(maxN)

    def __getNumPrimes(self, maxN:int) -> int:
        count = 0

        for i in range(1, maxN + 1):
            if PrimeDivisorsEnumerationOptimize.isPrime(i): 
                count += 1

        return count

    def __getNumPrimesBaseOnPrimes(self, maxN:int) -> int:
        count = 0
        primes = []

        for i in range(3, maxN + 1):
            if PrimeDivisorsEnumerationOptimize.isPrimeBaseOnPrimes(primes, i): 
                count += 1
                primes.append(i)

        return count + 1
