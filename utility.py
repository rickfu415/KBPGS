"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-25-2023
"""





def weighted_sections(vector):
    # Calculate the total sum of the vector
    total = sum(vector)
    
    # If the total is zero, return a vector of equal ranges
    if total == 0:
        equal_weight = 1/len(vector)
        return [(i*equal_weight, (i+1)*equal_weight) for i in range(len(vector))]

    # Calculate the weighted proportions
    proportions = [value/total for value in vector]
    
    # Convert proportions to cumulative sections
    ranges = []
    current = 0
    for proportion in proportions:
        ranges.append((current, current + proportion))
        current += proportion

    return ranges

def find_range(num, ranges):
    for idx, (start, end) in enumerate(ranges):
        if start <= num < end:
            return idx
    return -1  # if the number is not within any range

