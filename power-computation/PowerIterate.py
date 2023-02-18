def powerIterate(a:float, b:int) -> float:
    i = b
    result = 1

    while(i > 0):
        result *= a
        i -= 1

    return result