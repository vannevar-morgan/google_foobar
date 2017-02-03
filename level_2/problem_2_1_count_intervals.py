#! /usr/bin/env python3

def answer(intervals):
    """
    Takes a list of pairs [start, end] and returns the total amount of (unique time) in the interval of all pairs.

    e.g.,
    Inputs: (int) intervals = [[1, 3], [3, 6]]
    Output: (int) 5

    Inputs: (int) intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
    Output: (int) 16
    """

    # Sort the intervals prior to merging
    intervals.sort()
    """
    Since the intervals are sorted,
    for all entries but the last:
      (beg1, end1), (beg2, end2),....
      if beg2 <= end1:
        merge the interval
    """
    i = 0
    while i < (len(intervals) - 1):
        if intervals[i+1][0] <= intervals[i][1]:
            if intervals[i+1][1] > intervals[i][1]:
                intervals[i][1] = intervals[i+1][1]
            intervals.pop(i+1)
        else:
            i += 1

    time_sum = 0
    for pair in intervals:
        time_sum += pair[1] - pair[0]

    return time_sum
    
