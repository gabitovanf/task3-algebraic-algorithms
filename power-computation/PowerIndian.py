def powerIndian(a:float, b:int) -> float:
    """
    Алгоритм возведения в степень через домножение
    "Индийский алгоритм" (?)
    """

    if a == 1 or b == 0: return 1
    if b == 1: return a

    result = 1
    if b % 2 > 0: result = a

    halfPow = powerIndian(a, b // 2)
    
    return result * halfPow * halfPow