#! /usr/bin/env python3

import math
import decimal
#from decimal import *

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
    decimal.getcontext().prec = 70
    n_min = 3
    n_max = 40
    x_min = 1
    y_min = 1

    # Check constraints on parameters.
    if n < n_min or n > n_max:
        return "0"
    #        raise ValueError("specified value for n is out of range... valid range for n is [" + str(n_min) + ", " + str(n_max) + "] but n = " + str(n))
    if x < x_min or x > n:
        return "0"
    #    raise ValueError("specified value for x is out of range... valid range for x is [" + str(x_min) + ", " + str(n) + "] but x = "+ str(x))
    if y < y_min or y > n:
        return 0
    #    raise ValueError("specified value for y is out of range... valid range for y is [" + str(y_min) + ", " + str(n) + "] but y = "+ str(y))

    # If the parameters have no solution, return "0"
    if x + y > n + 1:
        return "0"
    
    # Return a string representing the number of permutations.
    return str(decimal.Decimal(math.floor(calc_stirling(n - 1, x + y - 2) * calc_mult(x + y - 2, x - 1))))
#'{0:f}'.format(x/y)

def calc_mult(n, k):
    """
    """
    return decimal.Decimal(math.factorial(n)) / decimal.Decimal((math.factorial(k) * math.factorial(n - k)))

memo = {}

def calc_stirling(n, k):
    """
    Returns the Stirling number of the first kind, given n and k.
    s(n, k)
    
    Inputs:
    (int) n = number of elements
    (int) k = cycles
    
    Outputs:
    (decimal.Decimal) s = Stirling number of the first kind, s(n, k)
    
    The Stirling number of the first kind counts the number of
    permutations given n elements and k cycles.
    """
    if n == 0 or k == 0:
        return decimal.Decimal(n == k)
    """
    s = memo.get((n, k))
    if s:
        return s
    """
    if (n, k) in memo:
        return memo[n, k]
    
    memo[n, k] = decimal.Decimal((n - 1) * calc_stirling(n - 1, k) + calc_stirling(n - 1, k - 1))
    return memo[n, k]
