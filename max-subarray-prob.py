# Problem - Given an array find the contigous sub array that has the maximum sum
# Example - Given the following array 
#		[-2,-1,2,5,-3,4]
# 	    The sub array that has the maximum sum is [2,5,-3,4]
# 	    Also the maximum sum is 8



# Brute force solution of the problem 
# In this appraoch we find all the possible sub arrays in the 

def max_subarray_sum_brute(arr):
    global_max = float('-inf')
    result_arr = []
    l = len(arr)
    
    for i in range(0,l-1):
        current_max = float('-inf')
        
        for j in range(i,l-1):
            if i==j:
                current_max = arr[i]
            else:
                current_max += arr[j]
            global_max = max(current_max, global_max)
    
    return global_max, result_arr





# driver code

def main():
    arry = [-2,-1,2,5,-3,4]
    result, sub_arr = max_subarray_sum_brute(arry)

    print(result)
    print(sub_arr)


main()