# ---------------------- Problem Statement -------------------------
# Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.
# Some numbers may appear twice.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]
 
# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# 
# Source :
# Leetcode and Geeks for Geeks
# ----------------------------------------------------------------------------




# ----------------------------- Brute force solution --------------------------------------
# The array has number between 1 to n also the array length is n
# this means that we can loop through 1 - n and then for each number from 1-n search the entire array to 
# find which is missing. 

# Time complexity of the solution would be O(n^2) because for each number from 1-n we search the whole array
# which would be of time complexity of O(n), since this is an unsorted array. 
# Going from 1 - n would be of time complexity O(n)
# Hence, total time complexity would be O(n) * O (n) which eqauls to O(n^2)

# Space complexity is O(1) as we are not stroring any additional array

# Steps :
# (1) Loop through numbers 1 to n where n is len of the array
# (2) For each number from 1 - n search the array if the number exists in the array 
# (3) If the number is i.e. if i == the current item of the array , mark seen falg as true and break out of array
# (4) If the seen flag is false then the number was not seen/ found in the array , hence add it to result
# (5) return the resulting array
# --------------------------------------------------------------------------------------------

def find_dissapearing_numbers_slow(nums : list)-> list:
    n = len(nums)
    result : list = []

    for i in range(1,n+1):
        seen = False
        # do a liner search of the array
        # you can do a binary search which is log n time , 
        # but would require sorting which adds n log n time
        for item in nums:
            if item == i:
                seen = True
                break;
        
        if not seen:
            result.append(i)

    return result




# ----------------------------------- Efficient solution ------------------------------------------ 
# The array has 1 to n numbers and has a len of n
# Taking advantage of this info we can solve this problem in linear time

# Explanation of this below code and logic behind it :
# Since the array only contains numbers between 1 to n and the array size is n , each item in the array 
# can be rearded as an index of the array. All we need to do to solve this problem is figure of the missing 
# index of the array. In order to do that we visit each item i.e. index of the array and mark it as visited 
# If any pirticular index i.e. item of the array is not visted then the array index of the number is a missing number

# To mark a item of array as visited mark it negetive

# Implementation Steps : 
# (1) Loops through each item of the array
# (2) For each item get the index it represents by substracting the absolute value of that item from 1
# (3) Use this resulting number from step 2 to visit the item of the array at that location
# (4) Once visted mark the number as -ve
# (5) Scan the array again and find the elements that are not -ve
# (6) The number from step 5 are the ones not visited at all
# (7) The index + 1 of the number are the missing items / numbers from 1-n


# Time Complexity of this algo is O(n) i.e. linear 
# Space compleity is constant i.e. O(1)
# ----------------------------------------------------------------------------------------------------

def find_dissappearing_numbers_fast(nums : list) -> list:
    n = len(nums)
    result : list=[]

    for i in range(0,n):                       # O(n) time complexity
        index = abs(nums[i])-1
        if nums[index]>0:
            nums[index] = -nums[index]

    for j in range(0,n):                       # O(n) time complexity
        if nums[j]>0:
            result.append(j+1)

    return result





# Driver Code 
def main():
    test_input1 = [4,3,2,7,8,2,3,1]
    result1 = find_dissapearing_numbers_slow(test_input1)
    print(result1)

    test_input2 = [1,1]
    result2 = find_dissapearing_numbers_slow(test_input2)
    print(result2)

    test_input3 = [4,3,2,7,8,2,3,1]
    result3 = find_dissappearing_numbers_fast(test_input3)
    print(result3)

    test_input4 = [1,1]
    result4 = find_dissappearing_numbers_fast(test_input4)
    print(result4)


main()