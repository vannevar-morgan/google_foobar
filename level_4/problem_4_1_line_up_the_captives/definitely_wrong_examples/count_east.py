import math

def answer(y, n):
    if y == 1:
        return str(math.factorial(n - 1))

    if y == n:
        return "1"

    if y > n:
        return "0"

    delta = n - y
    return str(calcIWrap(y, delta))

def calcI(peaks, delta):
    if peaks == 1:
        return math.factorial(delta)
    
    total = 0
    for i in range(0, delta + 1):
        left = math.factorial(i)
        right = calcI(peaks - 1, delta - i)
        print("peaks: " + str(peaks) + "\ti: " + str(i) + "\tdelta: " + str(delta) + "\tleft: " + str(left) + "\tright: " + str(right))
        total += left * right
    return total

def calcIWrap(peaks, delta):
    total = 0
    for i in range(peaks, 0, -1):
        total += calcI(i, delta)
    return total
    
