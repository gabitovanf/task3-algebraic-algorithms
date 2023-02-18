def FibonacciIteration(num:int) -> int:
    if num == 0: return 0
    if num == 1: return 1

    fiboPrev = 0
    fibo = 1

    for i in  range(2, num + 1):
        sum = fiboPrev + fibo
        fiboPrev = fibo
        fibo = sum

    return fibo