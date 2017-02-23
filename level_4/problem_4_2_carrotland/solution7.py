#! /usr/bin/python2.7

from __future__ import division
from fractions import Fraction


def answer(coords):
    """
    Calculate the number of points (with integer coordinates) 
    interior to the triangle specified by coords.
    
    The interior points are counted using Pick's Theorem.
    https://en.wikipedia.org/wiki/Pick%27s_theorem
    
    Input:
      coords - List of 3 coordinates, [x, y] with each coordinate represented as a list.
               Each coordinate represents a vertex of the triangle.
               Each vertex will have integer coordinates.
    
    Output:
      Number of points (with integer coordinates) interior to the triangle.
      A point is not interior to the triangle if it lies on the border of the triangle
      i.e., on a line between any 2 of the 3 vertices.
    
    Note:
      It is guaranteed that the 3 vertices will not be collinear.
    """
    coord1 = coords[0]
    coord2 = coords[1]
    coord3 = coords[2]
    area = coord1[0] * (coord2[1] - coord3[1]) + coord2[0] * (coord3[1] - coord1[1]) + coord3[0] * (coord1[1] - coord2[1])
    area = abs(area / 2)
    interior_points = area - (calc_border_points(coords) / 2) + 1
    return int(interior_points)
    

def calc_border_points(coords):
    """
    Return the number of border points.
    
    Input:
      coords - List of 3 coordinates, [x, y] with each coordinate represented as a list.
               Each coordinate represents a vertex of the triangle.
               Each vertex will have integer coordinates.

    Output:
      Number of points (with integer coordinates) that lie on the border of the triangle.
    
    Note:
      It is guaranteed that the 3 vertices will not be collinear.
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
    """
    Calculate the slopes of lines (12), (13), (23).
    A line with infinite slope is represented with slope = None
    """
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
    
    """
    Calculate the number of points (with integer coords) on each line using the line slopes.
    If the slope is infinite (a vertical line) then the number of points is the delta-y between the two points.
    """
    line12_points = 0
    line13_points = 0
    line23_points = 0
    if slope12 != None:
        line12_points = abs(x1 - x2) / slope12.denominator
    else:
        line12_points = abs(y1 - y2)
    if slope13 != None:
        line13_points = abs(x1 - x3) / slope13.denominator
    else:
        line13_points = abs(y1 - y3)
    if slope23 != None:
        line23_points = abs(x2 - x3) / slope23.denominator
    else:
        line23_points = abs(y2 - y3)
    
    # print("# of points on line12: " + str(line12_points))
    # print("# of points on line13: " + str(line13_points))
    # print("# of points on line23: " + str(line23_points))

    return line12_points + line13_points + line23_points


c1 = [-1, -1]
c2 = [0, 1]
c3 = [1, 0]
# c1 = [91207, 89566]
# c2 = [-88690, -83026]
# c3 = [67100, 47194]
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
# c1 = [0,0]
# c2 = [3,0]
# c3 = [4,3]
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

print(answer(a))
