class PrimeDivisorsEnumeration:
    @staticmethod
    def isPrime(a:int) -> bool:
        dividorsCount = 0
        dividor = a

        while (dividor > 0):
            if a % dividor < 1: dividorsCount += 1
            dividor -= 1

        return dividorsCount == 2

    def getNumPrimes(self, maxN:int) -> int:
        count = 0

        for i in range(1, maxN + 1):
            if PrimeDivisorsEnumeration.isPrime(i): 
                count += 1

        return count