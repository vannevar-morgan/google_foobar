#! /usr/bin/python3.4

import sys
import numbers
import math
from fractions import Fraction

def answer(coords):
    coord1 = coords[0]
    coord2 = coords[1]
    coord3 = coords[2]
    print(str(coord1[0]) + ", " + str(coord1[1]))
    print(str(coord2[0]) + ", " + str(coord2[1]))
    print(str(coord3[0]) + ", " + str(coord3[1]))
    area = coord1[0] * (coord2[1] - coord3[1]) + coord2[0] * (coord3[1] - coord1[1]) + coord3[0] * (coord1[1] - coord2[1])
    area = abs(area / 2)
    print("area before calc_ints(): " + str(area))
    area = area - calc_ints(coords)
    return max(0, area)
    #return math.floor(area)
    

def calc_ints(coords):
    """
    prints the count of points where a point on a line has integer coords.
    """
    coord1 = coords[0]
    coord2 = coords[1]
    coord3 = coords[2]
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    x3 = coord3[0]
    y3 = coord3[1]
    slope12 = None
    slope13 = None
    slope23 = None
    try:
        slope12 = Fraction((y2 - y1), (x2 - x1)) # slope of line connecting points 1 and 2
    except ZeroDivisionError:
        pass
    try:
        slope13 = Fraction((y3 - y1), (x3 - x1)) # slope of line connecting points 1 and 3
    except ZeroDivisionError:
        pass
    try:
        slope23 = Fraction((y3 - y2), (x3 - x2)) # slope of line connecting points 2 and 3
    except ZeroDivisionError:
        pass
    
    print("slope12: " + str(slope12))
    print("slope13: " + str(slope13))
    print("slope23: " + str(slope23))
    b12 = None
    b13 = None
    b23 = None
    if slope12 != None:
        b12 = y1 - slope12 * x1
    if slope13 != None:
        b13 = y1 - slope13 * x1
    if slope23 != None:
        b23 = y3 - slope23 * x3
    print("b12: " + str(b12))
    print("b13: " + str(b13))
    print("b23: " + str(b23))
    x12_range = []
    x13_range = []
    x23_range = []
    if slope12 != None:
        if x1 < x2:
            x12_range = range(x1, x2 + 1, slope12.denominator)
        else:
            x12_range = range(x2, x1 + 1, slope12.denominator)
    if slope13 != None:
        if x1 < x3:
            x13_range = range(x1, x3 + 1, slope13.denominator)
        else:
            x13_range = range(x3, x1 + 1, slope13.denominator)
    if slope23 != None:
        if x2 < x3:
            x23_range = range(x2, x3 + 1, slope23.denominator)
        else:
            x23_range = range(x3, x2 + 1, slope23.denominator)

    print("x23_range:")
    for x in x23_range:
        y_val = (x * slope23) + b23
        print("x: " + str(x) + "\ty23: " + str(y_val))
        
    count = 0 # number of border points that can't be built on
    if slope12 and slope13 and slope23:    
        count += len(x12_range)
        count += len(x13_range)
        count += len(x23_range)
        count -= 6 # 2 points for each line representing the vertices given.
    elif (not slope12 and not slope13):
        if slope12 is None:
            count += abs(y2-y1) + 1
        else:
            count += abs(y3-y1) + 1
    elif (not slope12 and not slope23):
        if slope12 is None:
            count += abs(y2-y1) + 1
        else:
            count += abs(y3-y2) + 1
    elif (not slope13 and not slope23):
        if slope13 is None:
            count += abs(y3-y1) + 1
        else:
            count += abs(y3-y2) + 1
    elif (not slope12):
        count += abs(y2-y1) + 1
        count -= 2
    elif (not slope13):
        count += abs(y3-y1) + 1
        count -= 2
    elif (not slope23):
        count += abs(y3-y2) + 1
        count -= 2

    # if slope12 is None:
    #     count += abs(y2-y1) + 1
    #     print("slope12 vertical: " + str(abs(y2-y1) + 1))
    # if slope13 is None:
    #     count += abs(y3-y1) + 1
    #     print("slope13 vertical: " + str(abs(y3-y1) + 1))
    # if slope23 is None:
    #     count += abs(y3-y2) + 1
    #     print("slope23 vertical: " + str(abs(y3-y2) + 1))
    # print("count: " + str(count))
    count = max(0, count)

    print("size x12_range: " + str(len(x12_range)))
    print("size x13_range: " + str(len(x13_range)))
    print("size x23_range: " + str(len(x23_range)))

    return count

c1 = [-1, -1]
c2 = [0, 1]
c3 = [1, 0]
c1 = [91207, 89566]
c2 = [-88690, -83026]
c3 = [67100, 47194]
# c1 = [1000000000, 1000000000]
# c2 = [-1000000000, -1000000000]
# c3 = [0,2]
# c1 = [2, 3]
# c2 = [6, 9]
# c3 = [10, 160]
# c1 = [15,15]
# c2 = [23,30]
# c3 = [50,25]
# c1 = [0, 0]
# c2 = [1000, 1]
# c3 = [1000, -1]
c1 = [0,0]
c2 = [3,0]
c3 = [4,3]
# c1 = [0,0]
# c2 = [3,0]
# c3 = [3,3]
# c1 = [0,0]
# c2 = [4,0]
# c3 = [4,4]
# c1 = [0,0]
# c2 = [4,0]
# c3 = [5,4]


a = [c1, c2, c3]

ans = answer(a)
print("answer: " + str(ans))
#calc_ints(a)
