def powerBinaryDecomposition(a:float, b:int) -> float:
    i = b
    curFactor = a
    result = 1

    if i % 2 > 0:
        result *= curFactor

    while(i > 1):
        i //= 2
        curFactor = curFactor * curFactor
        
        if i % 2 > 0:
            result *= curFactor

    return result