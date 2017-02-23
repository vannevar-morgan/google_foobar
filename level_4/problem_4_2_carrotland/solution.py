#! /usr/bin/python3.4

import sys
import numbers
import math

def answer(coords):
    coord1 = coords[0]
    coord2 = coords[1]
    coord3 = coords[2]
    area = coord1[0] * (coord2[1] - coord3[1]) + coord2[0] * (coord3[1] - coord1[1]) + coord3[0] * (coord1[1] - coord2[1])
    area = abs(area / 2)
    print("area before calc_ints(): " + str(area))
    area = area - calc_ints(coords)
    print("area: " + str(area))
    return math.floor(area)
    

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
    slope12 = (y2 - y1) / (x2 - x1) # slope of line connecting points 1 and 2
    slope13 = (y3 - y1) / (x3 - x1) # slope of line connecting points 1 and 3
    slope23 = (y3 - y2) / (x3 - x2) # slope of line connecting points 2 and 3
    print("slope12: " + str(slope12))
    print("slope13: " + str(slope13))
    print("slope23: " + str(slope23))
    b12 = y1 - slope12 * x1
    b13 = y1 - slope13 * x1
    b23 = y3 - slope23 * x3
    print("b12: " + str(b12))
    print("b13: " + str(b13))
    print("b23: " + str(b23))
    count = 0
    y_val = 0
    x12_range = []
    x13_range = []
    x23_range = []
    if x1 < x2:
        x12_range = range(x1, x2 + 1)
    else:
        x12_range = range(x2, x1 + 1)
    if x1 < x3:
        x13_range = range(x1, x3 + 1)
    else:
        x13_range = range(x3, x1 + 1)
    if x2 < x3:
        x23_range = range(x2, x3 + 1)
    else:
        x23_range = range(x3, x2 + 1)
    
    for i in x12_range:
        y_val = ((slope12 * i) + b12)
        if y_val == math.floor(y_val):
            count += 1
            # print("incremented, y_val: " + str(y_val) + "\ti: " + str(i))
        # if isinstance(y_val, numbers.Integral):
        #     count += 1
        if i == x1 or i == x2:
            count -= 1
            # print("decremented, y_val: " + str(y_val) + "\ti: " + str(i))
    for i in x13_range:
        y_val = ((slope13 * i) + b13)
        if y_val == math.floor(y_val):
            count += 1
            # print("incremented, y_val: " + str(y_val) + "\ti: " + str(i))
        if i == x1 or i == x3:
            count -= 1
            # print("decremented, y_val: " + str(y_val) + "\ti: " + str(i))
    for i in x23_range:
        y_val = ((slope23 * i) + b23)
        if y_val == math.floor(y_val):
            count += 1
            # print("incremented, y_val: " + str(y_val) + "\ti: " + str(i))
        if i == x2 or i == x3:
            count -= 1
            # print("decremented, y_val: " + str(y_val) + "\ti: " + str(i))
    print("count: " + str(count))
    return count

# c1 = [-1, -1]
# c2 = [1, 0]
# c3 = [0, 1]
c1 = [91207, 89566]
c2 = [-88690, -83026]
c3 = [67100, 47194]
# c1 = [1000000000, 1000000000]
# c2 = [-1000000000, -1000000000]
# c3 = [2, 2]
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
a = [c1, c2, c3]

ans = answer(a)
print("answer: " + str(ans))
#calc_ints(a)
