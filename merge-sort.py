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
# ..................................................................
# Implementaion Steps :
# (1) find the whole length of the arrary
# (2) if   : the array is shorter than or equal to 1 then just return the array back
#     else : go to step 3 
# (3) split the array in 2 halves 
# (4) perform merge sort for each half i.e. call merge sort recursively for each side
# (5) merge the resulting arrays back - merge is a helper function which drives the logic
#  ..................................................................................
#  Logic of Merge 
# (1) to merge two arrays in sorted order first initalize two pointers at the zero position of both arrays
# (2) while both pointers are smaller than the size of the left and right array
#       (a) compare the left element and right element 
#       (b) which ever is smaller intert that and increment the pointer for that array
# (3) One array might be longer than other , so append the rest of the longer array to the list
# (4) return the result , which should be a sorted array
#  ...................................................................................
# Explanation for time complexity of O(n log n) :
# The merge sort is a divde and conqure recursive algo
# This means that it forms a tree like structure if which lets say is of height (log n) 
#  where n is total no of elements in the array
# and at every level we perfrom n no. of merge operations of 
# ------------------------------------------------------------------------------

def merge_sort(arr:list) -> list:
    length = len(arr)

    # if length of the array is 1 or less than 1 then return the array
    if length>1:
        middle = length//2
        
        # divide the array up into two halves
        # left half start from 0 to rght before middle (excludes middle)
        # right half starts at middle and ends at last index
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        
        # call merge sort on each part 
        # for left the merge sort should start from first index to the index before middle postion
        # for right the merge sort should start from middle index to end index (not the length of the arr)
        left_sorted_arr = merge_sort(left_arr)
        right_sorted_arr = merge_sort(right_arr)
        
        # merge both sides
        return merge(left_sorted_arr, right_sorted_arr)
    else :
        # if length is less than or equal to one then return the array itself
        # no need to do any other operation
        return arr



# Helper Method - merge
# merges both halfs of the arrary in sorted order
def merge(left_list:list, right_list:list) ->list:
    left,right= 0,0

    result_arr:list  = []

    while left<len(left_list) and right <len(right_list):
        if left_list[left] >= right_list[right]:
            result_arr.append(right_list[right])
            right+=1
        else:
            result_arr.append(left_list[left])
            left+=1

    if(left<len(left_list)):
        result_arr.extend(left_list[left:len(left_list)])

    if(right<len(right_list)):
        result_arr.extend(right_list[right:len(right_list)])

    return result_arr
    
    



# Driver Code
def main():
    # Test Case 1 - Medium case , some elements are in order and other are not
    input_arr_1 = [12,11,13,5,6,7]
    sorted_arry_1 = merge_sort(input_arr_1)
    print(sorted_arry_1)

    # Test Case 2 - Worst case , entire array is inverted or in descending order
    input_arr_2 = [10,8,7,6,5,4,3,2,1]
    sorted_arry_2 = merge_sort(input_arr_2)
    print(sorted_arry_2)

    # Test Case 3 - Best case , the array is already sorted
    input_arr_3 = [20,30,40,50,60,100]
    sorted_arry_3 = merge_sort(input_arr_3)
    print(sorted_arry_3)


main()