def FibonacciRecursion(num:int) -> int:
    if num == 0: return 0
    if num == 1: return 1

    return FibonacciRecursion(num - 2) + FibonacciRecursion(num - 1)