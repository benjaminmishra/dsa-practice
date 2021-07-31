# ---------------------- Problem -------------------------------------------------- 
# Given an array find the contigous sub array that has the maximum sum
# Example - Given the following array 
#		[-2,-1,2,5,-3,4]
# 	    The sub array that has the maximum sum is [2,5,-3,4]
# 	    Hence, the maximum sum is 8
# ----------------------------------------------------------------------------------


# --------------------------- Brute force solution ---------------------------------
# In this appraoch we find all the possible sub arrays in the given array
# Method to find all possible sub arrays is to iterate through each item
# Then keep adding rest of the items to the item one by one in a loop

# Time Complexity O(n^2) - this is beacuse of the two nexted loops
# Space Complexity O(1) - Constant as we need to only store a few things and its not a ever increasing list

def max_subarray_sum_brute(arr):
    global_max = float('-inf')
    l = len(arr)
    
    for i in range(0,l):                               # loop through each item in the array
        current_max = float('-inf')
        
        for j in range(i,l):                           # for each item then add other items in the array to create a subarray
            if i==j:                                     # this is done to avoid summing the same item with itself
                current_max = arr[i]
            else:
                current_max += arr[j]                    # sum of the sub array by adding the sum of last sub array to create the new sum
            global_max = max(current_max, global_max)    # compare the current sum with the global max , which ever is greater take that
    
    return global_max



# ------------------- Linear Time Solution - Kadane's Algorithm-------------------------
# The last was a solution that would take a lot of time if the input was large
# Since this is an array it is possible to have a linear time solution i.e. O(n)
# The algo for that is named as Kadane’s Algorithm . This algo follows a dynamic programming (DP) appraoch
# 
# Approach :
# Foreach item in the array find the max sub array sum upto that item in the array 
# This is done by finding the max sum right up until the element before the current element
# Then adding the current element to that max and checking if that creates a new overall max or not
# If it creates a new over all max then repeat the same thing for the next element
# If it does not create a new overall max then start the process allover again from the current element
# 
# This is DP appraoch beacuse there are overlapping sub problems the result of which can be reused to solve
# the overall problem.
# The sub problem is finding the max subarray sum up until the current element 



def max_subarray_sum(arr):
    global_max_sum = float('-inf')
    curr_max_sum = 0
    l = len(arr)

    for i in range(0,l):
        curr_max_sum = max(arr[i], curr_max_sum+arr[i])
        global_max_sum = max(global_max_sum, curr_max_sum)

    return global_max_sum

# driver code
def main():
    arry = [-2,-1,2,5,-3,4]
    result1= max_subarray_sum_brute(arry)
    result2= max_subarray_sum(arry)

    print("Brute Force Result : " + result1)
    print("Kadane's Algo Linar Time: " + result2)


main()