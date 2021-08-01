# ------------------------------ Problem ------------------------------------------------
# Count inversions in an array i.e. how far is the array from being sorted
# 
# Details : From GeeksForGeeks - (https://www.geeksforgeeks.org/counting-inversions/)
# Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
#
# If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, 
# the inversion count is the maximum. 
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
# 
# Example :
# Input: arr[] = {8, 4, 2, 1}
# Output: 6
#
# Explanation: Given array has six inversions:
# (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
#
#
# Input: arr[] = {3, 1, 2}
# Output: 2
#
# Explanation: Given array has two inversions:
# (3, 1), (3, 2) 
#
# Questions to Ask :
# Are there any duplicates in the given array (nope , all unique)
# ---------------------------------------------------------------------------------



# --------------------- Simple or Brute force approach ----------------------------
# This solution basically traveses through the array twice and has O(n^2) time complexity
#
# Explanation :
# For every item in the array we check if the items that come after it are smaller than it or not
# If they are smaller then it means we need to swap the element with the one smaller than it to make the array sorted.
# If they are not smaller than current element then no need to swap
# We initalize a counter in order to keep track of the number of swaps required, its incremented whenever we see that a 
# swap is needed.
#
# This is a quadaratic time complexity because we have two nested for loops
# and in worst case i.e. if the array is in the opposite order then every element needs to be swapped n time
# making it n*n i.e. n^2 time complexity
# Space Complexity : O(1) i.e. constant as we just store the counter value and update it in place
#---------------------------------------------------------------------------------------

def count_inversions_simple(arr : list) -> int:
    length = len(arr)

    inversion_counter = 0                          # start counter that keeps tracks of number of swaps required

    for i in range(0,length):                      # first loop to go through each element in the array
        for j in range(i+1, length):               # second loop , start from the element that is on the right of the current element
            if arr[i]>arr[j]:                      # if current element larger than the element it is being compared with then 
                inversion_counter+=1               # increase counter , otherwise do nothing and move on
    
    return inversion_counter




# ------------------------------ Divde and Conqure Method (Enhanced Merge Sort) -----------------------------
# The idea is to divide the array into smaller parts and get the invversion count in each part
# Explanation and Steps :


def count_count_inversions_merge_sort(arr:list) ->int:
    pass



# Driver code
def main():
    # test 1 - worst case scenario , i.e. the array is in the decending order
    input_arr_1 = [8, 4, 2, 1]
    result_1 = count_inversions_simple(input_arr_1)
    print(result_1)

    # test 2 - medium case , i.e some elements are in order other need to be swapped
    input_arr_2 = [3,1,2]
    result_2 = count_inversions_simple(input_arr_2)
    print(result_2)

    # test 3 - best case , everything is in ascending order
    input_arr_3 = [4,5,6,7,8,9,10]
    result_3 = count_inversions_simple(input_arr_3)
    print(result_3)


main()