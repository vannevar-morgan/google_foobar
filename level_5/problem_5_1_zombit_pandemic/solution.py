#! /usr/bin/env python3

import sys
from fractions import Fraction
from math import factorial

memo_oeis_a000435 = {}
memo_binomial = {}


def calc_warren_sizes(n):
    """
    return the possible warren sizes for n rabbits.
    i.e., the ways to split the rabbits into warrens.
    each rabbit nudges 1 other rabbit so min warren size is 2.
    """
    warrens = []
    warrens.append([n])
    for i in range(2, n//2 + 1):
        warrens.append([i, n - i])
    return warrens


def get_warren_size_map(n):
    """
    return a map of num rabbits to possible warren sizes
    """
    w_sizes = {}
    for i in range(2, n + 1):
        w_sizes[i] = calc_warren_sizes(i)
    return w_sizes


def expand_partitions(size_map):
    """
    size_map: map of number of rabbits to possible warren partitions

    substitute (append to the list) partitions where a warren in a partition can be expressed as a multiplicity of a lower order.
    i.e., [2,4] can also be represented as [2, 2, 2]
    """
    keys = size_map.keys()
    min_n = min(keys)
    max_n = max(keys)
    if max_n < 6:
        # no splits can be expanded at n < 6
        return
    
    # for i in range(6, max_n + 1):
    for i in range(max_n, max_n + 1):
        current = size_map[i][1:]
        partition_hash = {}
        for p in current:
            partition_hash[tuple(p)] = True
        # for each partition for the current number of rabbits...
        p = 0
        while p < len(current):
            partition = current[p]
            # for each warren in the partition...
            for w in range(0, len(partition)):
                if partition[w] > 3:
                    # then the partitions for total rabbits = w must be substituted in size_map[partition[w]][1:] for partition[w]
                    subs = size_map[partition[w]][1:]
                    temp = partition[0:w] + partition[w+1:]
                    for s in subs:
                        temp2 = sorted(temp + s)
                        temp3 = tuple(temp2)
                        if temp3 not in partition_hash:
                            current.append(temp2)
                            partition_hash[temp3] = True
            p += 1
        size_map[i][1:] = current
    return


def binomial(n, k):
    """
    binomial function, n choose k
    (there are better ways to compute the binomial function but this is suitable for n = [2 - 50])
    """
    if (n, k) in memo_binomial:
        return memo_binomial[(n, k)]
    else:
        memo_binomial[(n, k)] = factorial(n) // (factorial(k) * factorial(n - k))
    return memo_binomial[(n, k)]


def t(n):
    """
    return OEIS A000435 for n (OEIS A001864 / n)
    (counts the number of ways of connecting n labelled nodes)
    """
    if n in memo_oeis_a000435:
        return memo_oeis_a000435[n]
    else:
        s = 0
        for k in range(1, n):
            s += binomial(n, k) * ((n - k) ** (n - k)) * (k ** k)
        memo_oeis_a000435[n] = s // n
        return s // n


def T(partition):
    """
    return product of t(p) for all p in partition<p0,p1,p2...,pn>
    (counts the number of ways of connecting the labelled nodes (rabbits) inside each connected component (warren) for all connected components (all warrens))
    """
    total = 1
    for p in partition:
        total *= t(p)
    return total


def c_num(n, partition):
    """
    calculate the numerator for C()
    """
    total = 1
    for p in partition:
        total *= binomial(n, p)
        n -= p
    return total


def c_den(partition):
    """
    calculate the denominator for C()
    """
    total = 1
    s = set(partition)
    for p in s:
        total *= factorial(partition.count(p))
    return total


def C(n, partition):
    """
    return the number of ways n labelled items can be split according to a partition
    """
    return Fraction(c_num(n, partition) / c_den(partition))


def numerator(n, partitions):
    """
    calculate the numerator
    """
    total = 0
    for p in partitions:
        m = max(p)
        c_val = C(n, p)
        t_val = T(p)
        total += max(p) * C(n, p) * T(p)
    return total


def denominator(n):
    """
    calculate the denominator
    """
    return Fraction((n - 1) ** n, 1)


def answer(n):
    """
    calc expected number of rabbits infected.
    """
    if n is 2:
        return "2/1"
    elif n is 3:
        return "3/1"
    else:
        partitions_map = get_warren_size_map(n)
        expand_partitions(partitions_map)
        num = numerator(n, partitions_map[n])
        den = denominator(n)
        return str(num / den)
    


USAGE_MSG = "./solution.py n"
ERROR_MESSAGE_NBOUNDS = "n must be >= 2"

if len(sys.argv) != 2:
    print(USAGE_MSG)
    sys.exit(0)

n = int(sys.argv[1])
if n < 2:
    print(ERROR_MESSAGE_NBOUNDS)
    sys.exit(0)

print(answer(n))
