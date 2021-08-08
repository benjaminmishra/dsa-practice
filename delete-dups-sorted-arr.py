# ------------------------------- Problem Description ----------------------------
# Elements of Programming Interview : Problem 6.5 @ Page 65
# 
# Delete duplicates from a sorted array :
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. More formally, 
# if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. 
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# 
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Constraints:
# (1) 0 <= nums.length <= 3 * 104
# (2) -100 <= nums[i] <= 100
# (3) nums is sorted in non-decreasing order.
# ---------------------------------------------------------------------------------


# ----------------------------- Effiecient Solution O(n)--------------------------------
# Two pointer solution
# Initialize a pointer i which keeps track of current element
# Do a for loop on rest of the array with j, whenever you encounter that arr[i] != arr[j], do following
# (1) increment i to point to next element 
# (2) assign the element j points to onto i element in the array
# (3) start incrementing j all over again and do same steps until j reaches end of array
# (4) retrun the i+1 position, since this is the part of the array that now has unique number rest is useless
#
# Time Complexity: O(n) - Since there is one for loop only 
# i.e. we are going through the array only once
#
# Space Complexity: O(1) - We don't store anything extra except l and i which is constant 
#------------------------------------------------------------------------------------

def del_duplicates_efficient(nums : list[int])-> int:
    l : int = len(nums)
    i : int = 0
    
    for j in range(1,l):
        if nums[i]!=nums[j]:
            i+=1
            nums[i] = nums[j]

    return i+1




# Driver Code

def main():
    input_1 : list[int] = [1,1,2]
    print(input_1)
    result_1 = del_duplicates_efficient(input_1)
    print(input_1[:result_1])


main()
