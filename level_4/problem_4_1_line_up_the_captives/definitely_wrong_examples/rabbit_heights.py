#! /usr/bin/env python3

def answer(x, y, n):
    import math
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

    # unique peaks are rabbits which are seen, 1 is seen by both sides.
    peaks = x + y - 1
    if peaks < 2:
        return "0"
    
    # free rabbits are those which can be placed between peaks.
    free = n - peaks
    
    #    fList = getValleys(x, y, n)
    if peaks == 2:
        alpha = 1
    else:
        alpha = free + 1
    perms = alpha * math.factorial(free)
    for i in range(0, alpha - 1):
        perms += (free**i) * math.factorial(free - 1)
    return perms
        
        
    

#def getValleys(x, y, n):
    """
    Returns a list of the sizes of all possible valleys given n heights and x, y left and right peaks.

    Inputs:
    (int) 
    """
