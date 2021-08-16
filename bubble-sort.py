

# ------------------------------- Problem Description ----------------------------
# Write the Bubble Sort Alorithm
# ---------------------------------------------------------------------------------




# -----------------------------  Solution --------------------------------
# Simplest algorithm for sorting an array/list
# It works by constantly swpping two adjcent elements in the array in case they are out of order
# This operation needs to be performed for all positions of the array in order to sort the entire array

# Time Complexity: O(n^2) 
#
# Space Complexity: O(1) , constant
#------------------------------------------------------------------------------------

def bubble_sort(arr : list[int]) -> list[int]:
    n : int = len(arr)  # length of the array

    # we need to run the comparision for all positions in the array
    for j in range(n):
        # for each item in the array
        # check if that item is greater than the next item
        # if yes then swap otherwise move on to next

        # do this comparision only upto the n-1-j because the last item is already sorted
        for i in range(n-1-j):
            if arr[i] > arr[i+1]:
                # swap
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp

    return arr

    



# Driver Code

def main():
    # Test Case 1 - Medium case , some elements are in order and other are not
    input_arr_1 = [12,11,13,5,6,7]
    sorted_arry_1 = bubble_sort(input_arr_1)
    print(sorted_arry_1)

    # Test Case 2 - Worst case , entire array is inverted or in descending order
    input_arr_2 = [10,8,7,6,5,4,3,2,1]
    sorted_arry_2 = bubble_sort(input_arr_2)
    print(sorted_arry_2)

    # Test Case 3 - Best case , the array is already sorted
    input_arr_3 = [20,30,40,50,60,100]
    sorted_arry_3 = bubble_sort(input_arr_3)
    print(sorted_arry_3)



main()