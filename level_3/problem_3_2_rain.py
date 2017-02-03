#! /usr/bin/env python3

def answer(heights):
    """
    Takes a list of ints representing the heights of the hutches and
    calculates the total amount of water accumulated on the bunnie hutches.

    Note that the heights array will have at least 1 element and at most
    9000 elements.
    
    Note that each element will have a value of at least 1 and at most 100000.

    e.g.,
    Input:
      (int list) heights = [1, 4, 2, 5, 1, 2, 3]
    Output:
      int rain_total = 5
    
    """
    if len(heights) < 3:
        return 0 # No rain can accumulate because there are no local minima.
    
    rain_total = 0
    left_index = 1 # initialize to 1 so that the search for next decreasing starts at 0.
    right_index = 0
    
    while left_index < len(heights):
#        print(heights)
        # Find the index of the next decreasing value.
        left_index -= 1 # decrement the index so that the search for next decreasing starts on the peak.
        left_index += findNextDecreasing(heights[left_index::])
        
#        print("left_index: " + str(left_index) + "\tright_index: " + str(right_index) + "\tlen(heights): " + str(len(heights)) + "\train_total: " + str(rain_total))
        if left_index == len(heights):
            break # The entire range of bunny hutches has been counted.
        
        # Find the index of the next increasing value following the first decreasing value.
        right_index = left_index
        right_index += findNextIncreasing(heights[left_index::], heights[left_index])
        right_index += findNextDecreasing(heights[right_index::])
        
        # Sum the rainfall in this minima and update the heights since they've become filled with rain.
#        print("left_index: " + str(left_index) + "\tright_index: " + str(right_index) + "\tlen(heights): " + str(len(heights)) + "\train_total: " + str(rain_total))
        # The datum_val is the value of the local max to the left or right.
        # It represents the lowest value to which troughs can be filled in this region.
        # Decrement 1 from each index to get the value at the peak.
        datum_val = min(heights[left_index - 1], heights[right_index - 1])
#        print("datum_val: " + str(datum_val))
        for i in range(left_index, right_index - 1): # left_index already points 1 past the peak, no need to decrement.
            if datum_val > heights[i]:
                rain_total += datum_val - heights[i]
                heights[i] = datum_val
        
        if right_index == len(heights):
#            print(heights)
            break # The remaining bunny hutches do not increase in height so no more rain can collect in this region.

        # Update the index for the left bounding value.
        if heights[right_index - 1] >= heights[left_index - 1]:
            left_index = right_index - 1
    
    return rain_total

    
    
def findNextDecreasing(vals, datum_val = 0):
    """
    Increments an index while values are non-decreasing.
    """
    i = 0
    while i < len(vals):
        if vals[i] < datum_val:
            break
        else:
            datum_val = vals[i]
            i += 1
    
    return i


def findNextIncreasing(vals, datum_val):
    """
    Increments an index while values are non-increasing, starting from a datum value.
    """
    i = 0
    while i < len(vals):
        if vals[i] > datum_val:
            break
        else:
            datum_val = vals[i]
            i += 1
    
    return i
