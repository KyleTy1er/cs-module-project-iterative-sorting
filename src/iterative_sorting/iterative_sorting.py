


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(len(arr)):
        # Its called minimum index because it is the index location of the minimum value!
        min_index = i
        for x in range(i+1, len(arr)):
            if arr[min_index] > arr[x]:
                min_index = x
        # In this line we swap index values by solely referencing the index locations
        # saying arr[i] = arr[min_index] is the same as saying the value at this index location
        # needs to be replaced by the value at this other index location
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# In Bubble Sort, we make a series of swaps between adjacent elements, gradually moving larger elements towards the end of the array (or bubbling larger elements up).

# Loop through your array
# Compare each element to its neighbor
# If elements in wrong position (relative to each other, swap them)
# If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        current_index = i
        for x in range(i, len(arr)):
            if arr[i] > arr[x]:
                arr[i], arr[x] = arr[x], arr[i]
    return arr
'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
