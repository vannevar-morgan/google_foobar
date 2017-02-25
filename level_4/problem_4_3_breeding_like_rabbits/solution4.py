#! /usr/bin/python2.7

from __future__ import division
from decimal import Decimal
import sys


def answer(str_S):
    """
    Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a positive integer no greater than 10^25.
    """
    s = int(str_S)
    return find_n(s)


def find_n(s):
    """
    Return (as a Str) the greatest index, n, such that R(n) = s
    
    If no R(n) = s then "None" is returned. 
    """
    if s == 1:
        return "1"
    if s == 2:
        return "2"
    
    fibs = {}
    fibs[Decimal(0)] = 1
    fibs[Decimal(1)] = 1
    fibs[Decimal(2)] = 2

    # search the odd range, then search the even range, return the greater index, or None
    even_n = bin_search(fibs, s, Decimal(4))
    if even_n is None:
        return bin_search(fibs, s, Decimal(3))
    else:
        return even_n

    
    # if odd_n is None and even_n is None:
    #     return "None"
    # elif odd_n is None:
    #     return str(int(even_n))
    # else:
    #     return str(int(odd_n))
        


def bin_search(fibs, s, n_beg):
    """
    Perform binary search starting at index n_beg, to find R(n) == s
    """
    #print("bin_search: " + str(n_beg))
    offset = Decimal(0) # offset for even
    if n_beg % 2 != 0:
        offset = Decimal(1) # offset for odd
    
    # find the upper bound for n
    n_end = n_beg # upper bound for n
    build_fib_map(n_end, fibs)
    while fibs[n_end] < s:
        n_end = Decimal((n_end * 2) - offset)
        build_fib_map(n_end, fibs)

    if fibs[n_end] == s:
        return str(n_end)
    
    # find the lower bound for n
    n_beg = max(n_beg, (n_end + offset) / 2) # lower bound for n
    # build_fib_map(n_beg, fibs)

    # binary search to find n for R(n) == s
    while n_beg != n_end:
        # print("n_beg: {0:25f}".format(n_beg))
        # print("n_end: {0:25f}".format(n_end))
        if n_beg + 2 == n_end:
            build_fib_map(n_beg, fibs)
            build_fib_map(n_end, fibs)
            break
        n_mid = n_beg + (n_end - n_beg) / 2
        # print("n_mid: {0:25f}".format(n_mid))
        # print("range: {0:25f}".format(n_end - n_beg))
        # print("half_range: {0:25f}".format((n_end - n_beg)/2))
        build_fib_map(n_mid, fibs)
        if fibs[n_mid] < s:
            # print("less than")
            n_beg = n_mid
        elif fibs[n_mid] > s:
            # print("greater than")
            n_end = n_mid
        else:
            # print("equal")
            n_beg = n_mid
            n_end = n_mid
            break
    
    if fibs[n_end] == s:
        return n_end
    if fibs[n_beg] == s:
        return n_beg
    else:
        return None



def build_fib_map(n, fib_map):
    """
    """
    #    print("build fib map")
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

s_val = "7"
if len(a) == 2:
    s_val = a[1]

print(answer(s_val))
