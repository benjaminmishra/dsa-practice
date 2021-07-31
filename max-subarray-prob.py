# ---------------------- Problem -------------------------------------------------- 
# Given an array find the contigous sub array that has the maximum sum
# Example - Given the following array 
#		[-2,-1,2,5,-3,4]
# 	    The sub array that has the maximum sum is [2,5,-3,4]
# 	    Also the maximum sum is 8
# ----------------------------------------------------------------------------------


# Brute force solution -------------------------------------------------------------
# In this appraoch we find all the possible sub arrays in the given array
# Method to find all possible sub arrays is to iterate through each item
# Then keep adding rest of the items to the item one by one in a loop

# Time Complexity O(n^2) - this is beacuse of the two nexted loops
# Space Complexity O(1) - Constant as we need to only store a few things and its not a ever increasing list

def max_subarray_sum_brute(arr):
    global_max = float('-inf')
    result_arr = []
    l = len(arr)
    
    for i in range(0,l-1):                               # loop through each item in the array
        current_max = float('-inf')
        
        for j in range(i,l-1):                           # for each item then add other items in the array to create a subarray
            if i==j:                                     # this is done to avoid summing the same item with itself
                current_max = arr[i]
            else:
                current_max += arr[j]                    # sum of the sub array by adding the sum of last sub array to create the new sum
            global_max = max(current_max, global_max)    # compare the current sum with the global max , which ever is greater take that
    
    return global_max, result_arr





def max_subarray_sum(arr):
    pass




# driver code
def main():
    arry = [-2,-1,2,5,-3,4]
    result, sub_arr = max_subarray_sum_brute(arry)

    print(result)
    print(sub_arr)


main()