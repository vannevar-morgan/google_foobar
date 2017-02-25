#! /usr/bin/python2.7

import sys

def answer(str_S):
    """
    Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a positive integer no greater than 10^25.
    """
    # testing for now with ints...
    n = str_S
    vals = {}
    vals[0] = 1
    vals[1] = 1
    vals[2] = 2
    for i in range(1, n + 1):
        build_fib_map(i, vals, True)
    
    return vals[n]

def build_fib_map(n, fib_map, recurse = False):
    """
    """
    if n in fib_map:
        if n >= 1 and recurse:
            temp_val2 = build_fib_map(n - 1, fib_map) + fib_map[n] + 1
            fib_map[2 * n + 1] = temp_val2
        if n > 1 and recurse:
            temp_val1 = build_fib_map(n + 1, fib_map) + fib_map[n] + n
            fib_map[2 * n] = temp_val1
        return fib_map[n]
    else:
        print("n not in fib_map" + str(n))
        return 0

        


a = sys.argv

s_val = 7
if len(a) == 2:
    s_val = int(a[1])

print(answer(s_val))
