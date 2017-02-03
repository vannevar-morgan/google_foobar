#! /usr/bin/env python3

import math

def calc_i(y, i_max):
    """
    """
    if y == 1:
        return math.factorial(i_max)

    total = 0
    for i in range(0, y):
        total += math.factorial(i) * i_max * calc_i(y - 1, i_max - i)
        

    return total

