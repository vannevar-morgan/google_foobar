#! /usr/bin/env python3

import math

def answer(x, y, n):
    """
    Returns the number of possible ways to arrange n rabbits of unique heights
    along an east to west line, so that only x are visible from the west, and
    only y are visible from the east.
    
    The return value is a string representing the number in base 10.

    If there is no possible arrangement, the string "0" is returned.

    Assumptions:
       -The number of rabbits (n) will be as small as 3 or as large as 40
       -The viewable rabbits from either side (x and y) will be as small as 1
        and as large as the total number of rabbits (n)
    
    Inputs:
       (int) x = number of rabbits visible from the west.
       (int) y = number of rabbits visible from the east.
       (int) n = number of rabbits of unique heights.

    Outputs:
       (string) A string representing the number (in base 10) of ways to
                arrange the rabbits.
    
    e.g.,
    Inputs:
       (int) x = 2
       (int) y = 2
       (int) n = 3

    Output:
       (string) "2"

    Inputs:
       (int) x = 1
       (int) y = 2
       (int) n = 6

    Output:
       (string) "24"
    """
    n_min = 3
    n_max = 40
    x_min = 1
    y_min = 1

    # Check constraints on parameters.
    if n < n_min or n > n_max:
        raise ValueError("specified value for n is out of range... valid range for n is [" + str(n_min) + ", " + str(n_max) + "] but n = " + str(n))
    if x < x_min or x > n:
        raise ValueError("specified value for x is out of range... valid range for x is [" + str(x_min) + ", " + str(n) + "] but x = "+ str(x))
    if y < y_min or y > n:
        raise ValueError("specified value for y is out of range... valid range for y is [" + str(y_min) + ", " + str(n) + "] but y = "+ str(y))

    # Check if the parameters have no solution.
    if x + y > n + 1:
        return "0"


    # for now, solve the simpler case of only considering y
    if y == 1:
        return math.factorial(n - y)

    total = 0
    # for each peak...
    for i in range(0, y):
        # for each 
        total += iOp(i + 1, n - y)
        
    return total

def iOp(n, delta):
    """
    Performs an i-operation.

    Inputs:
    (int) n = number of iterations
    (int) delta = init value representing difference of total rabbits and rabbits which are seen.
    """
    if n == 0:
        return delta
    
    total = 0
    for i in range(0, delta):
        temp = math.factorial(i)
        for j in range(0, n):
            #print("Total: " + str(total) + "\tn: " + str(n) + "\tdelta: " + str(delta))
            temp *= iOp(n - 1, delta - i)
        total += temp
        
    return total
        
