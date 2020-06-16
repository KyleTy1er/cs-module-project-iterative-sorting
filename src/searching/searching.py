# Linear (Sequential) Search
#
# Sometimes referred to as sequential search, this algorithm is fairly straightforward. Given a set of data,
# traverse the dataset one item at a time until either you find the item you are looking for OR check every item in the
# set and verify the item you are looking for is not there.


def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(target)
    else:
        return -1   # not found




# Write an iterative implementation of Binary Search

# Binary Search
#
# The process of performing a binary search has a couple of extra steps.
# First, there is a precondition that the set of data you are searching is already sorted
# (alphabetically, numerically, etc). Then, the steps to search are:
#
# Compare the item in the middle of the data set to the item we are searching for.
# If it is the same, stop. We found it and are done!
# Else, if the item we are searching for is LESS than the item in the middle:
# Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
# Else, the item we are searching for is GREATER than the item in the middle:
# Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.


def binary_search(arr, target):
    lo = 0
    hi = len(arr)
    # Set boundaries for low and high marks to search
    # While low and high do not overlap...
    while lo < hi:
        # Check the midpoint
        # Divide in half
        mid = (lo + hi) // 2
        # If it's equal, return True
        if arr[mid] == target:
            return mid
        # Else if target is smaller,
        elif target < arr[mid]:
            # set the high to midpoint value
            hi = mid
       # Else if target is bigger,
        else:
            # set the low to midpoint value
            lo = mid + 1
    return -1
