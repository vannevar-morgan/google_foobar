#! /usr/bin/python2.7

from __future__ import division
import sys

def answer(str_S):
    """
    Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a positive integer no greater than 10^25.
    """
    # testing for now with ints...
    n = str_S
    fibs = {}
    fibs[0] = 1
    fibs[1] = 1
    fibs[2] = 2
    build_fib_map(n, fibs)
    
    return fibs[n]

def build_fib_map(n, fib_map):
    """
    """
    if n in fib_map:
        return fib_map[n]
    else:
        if n % 2 == 0:
            # even
            half_n = n / 2
            temp_val = build_fib_map(half_n, fib_map) + build_fib_map(half_n + 1, fib_map) + half_n
            fib_map[n] = temp_val
            return temp_val
        else:
            # odd
            half_n = (n - 1) / 2
            temp_val = build_fib_map(half_n, fib_map) + build_fib_map(half_n - 1, fib_map) + 1
            fib_map[n] = temp_val
            return temp_val


        


a = sys.argv

s_val = 7
if len(a) == 2:
    s_val = int(a[1])

print(answer(s_val))
