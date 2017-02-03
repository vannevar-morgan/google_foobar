#import math
from math import factorial

# used for memoization of recursively calculating sterling numbers
mem = {}


def memoize(key, func, *args):
    """
    Helper to memoize the output of a function
    """
    if key not in mem:
        # store the output of the function in memory
        mem[key] = func(*args)

    return mem[key]


def arrange(n, k):
    """
    Calculates the number of arrangements of 'n' rabbits
    where 'k' rabbits can be seen from the front.
    n = total number of rabbits
    k = number or rabbits that can be seen from the front
    """
    if k > n:
        # when the guard can see more rabbits than there are,
        # there are no possible valid arrangements
        return 0

    if k == n:
        # when the guard can see as many rabbits as there are,
        # there is only one arrangement (ordered)
        return 1

    if k == 1:
        # when the guard can only see one rabbit,
        # it's just the total number of permutations
        # of the rabbits behind the tallest one
        return factorial(n - 1)

    if k == n - 1:
        # when the guard can see one less than the number of rabbits,
        # the tallest has to be the second to last one, so it's just
        # the number of combinations there are of swapping the one that's
        # behind the tallest with one that's in front of the tallest.
        return combinations(n, 2)

    # memoize and return the result of the next level of recursion
    #
    # arrange(n - 1, k - 1):
    #   make one more rabbit visible by having the shortest rabbit at the front,
    #   so we're arranging (n - 1) rabbits to have (k - 1) visible.
    #
    # arrange(n - 1, k) * (n - 1):
    #   have the shortest rabbit in any (n - 1) position (not at the front), so
    #   k does not change because there will be a taller rabbit in front of it.
    return memoize(
        (n, k),
        lambda: arrange(n - 1, k - 1) + arrange(n - 1, k) * (n - 1),
    )


def combinations(n, k):
    """
    Returns the number of unique subsets of 'k' number of elements
    that can be chosen from a set of 'n' elements.
    Eg. combinations(3,2) = 3
    Unique subsets of size '2' that can be made from (1,2,3):
    (1,2), (1,3), (2, 3)
    """
    return factorial(n) / (factorial(k) * factorial(n - k))


def answer(x, y, n):
    """
    The concept here is to group the heights of the bunnies into subsets
    consisting of one rabbit, and all succeeding bunnies before the next
    visible rabbit. Excluding the tallest rabbit (n - 1), we'll have
    a total number of subsets equal to 'x + y - 2'. For example,
    Heights: 1,2,3,4, where x = 2 and y = 3 can be arranged as
        3,4,2,1 where the subsets are:
            --> [3],4,[2,1]
                [3,4],[2],[1] <--
        This shows that the number of subsets is equal to the number of
        bunnies that can be seen from that side.
    So all we need to do is calculate how many subsets there will be,
    and multiply that by the number of ways we can arrange those subsets.
    x = number of bunnies that can be seen from the left
    y = number of bunnies that can be seen from the right
    n = total number of bunnies
    """
    return str(math.floor(arrange(n - 1, x + y - 2) * combinations(x + y - 2, x - 1)))
