# ----------------------- Problem Description --------------------------------
# Given an array unsorted array sort it with merge sort algo
# Example :
# Input array : [12, 11, 13, 5, 6, 7]
# Output : [5,6,7,11,12,13]
# ----------------------------------------------------------------------------


# --------------------------  Solution ---------------------------------------
# Merge sort is an algorithm with O(n log n) time complexity 
# Space complexity is O(n)
# Also merge sort is an algo that creates a new array as a result
# 
# While merge sort is efficient in terms of time complexity but it is 
# bad in terms of space complexity.
# 
# It is also a divide and conqure algo , which breaks the problem into 
# smaller self replicating problems and solves them using resursion.

# Implementaion Steps 
# 
# ------------------------------------------------------------------------------



def merge_sort(arr:list, start_index:int, end_index:int) ->list:
    length = end_index-start_index+1
    middle = length/2

    left_arr = arr[0:middle]
    right_arr = arr[middle+1:length]

    

