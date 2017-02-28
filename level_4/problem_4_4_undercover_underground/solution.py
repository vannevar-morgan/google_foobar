#! /usr/bin/env python2.7

from __future__ import division
from math import factorial
import sys


def answer(n, k):
    """
    Return the number of graphs with n nodes and k edges.
    
    Input:
        (int) n = number of nodes
        (int) k = number of edges
    Output:
        (string) number of graphs with n nodes and k edges.
    """
    memo_table = {}
    return str(calc_ans(n, k, memo_table))


def calc_ans(n, k, memo):
    """
    Count the number of graphs with n nodes and k edges.
    
    Input:
        (int) n = number of nodes
        (int) k = number of edges
        (dict) memo = memo pad to memoize function
    Output:
        (long) number of graphs with n nodes and k edges.
    """
    if (n, k) in memo:
        return memo[(n, k)]
    
    if (k < n - 1) or (k > n * (n - 1) // 2):
        memo[(n, k)] = 0
        return 0
    
    if k == n - 1:
        memo[(n, k)] = int(n**(n - 2))
        return memo[(n, k)]
    
    res = calc_bin_coeff(n * (n - 1) // 2, k)
    for m in range(0, n - 1):
        res2 = 0
        for p in range( max(0, int(k - (m + 1) * m // 2)), (k - m + 1) ):
            res2 += calc_bin_coeff( (n - 1 - m) * (n - 2 - m) // 2, p) * calc_ans(m + 1, k - p, memo)
        
        res -= calc_bin_coeff(n - 1, m) * res2
    
    memo[(n, k)] = res
    return res
    

memo_bin_coeff = {}
def calc_bin_coeff(n, k):
    """
    Return the binomial coefficient for n, choose k.
    
    Input:
        (int) n = number of nodes
        (int) k = number of edges
    Output:
        (long) binomial coefficient for n, choose k.
    """
    if (n, k) in memo_bin_coeff:
        return memo_bin_coeff[(n, k)]
    
    if n - k < 0:
        memo_bin_coeff[(n, k)] = 0
        return 0
    temp = factorial(n) // (factorial(k) * factorial(n - k))
    memo_bin_coeff[(n, k)] = temp
    return temp
    


USAGE_MSG = "usage: ./solution n k"

n = 2
k = 1
if len(sys.argv) == 3:
    n = int(sys.argv[1])
    k = int(sys.argv[2])
else:
    print(USAGE_MSG)
    sys.exit(0)

print(answer(n, k))
