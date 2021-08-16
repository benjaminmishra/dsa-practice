
# ------------------------------- Problem Description ----------------------------
# Implement Binary Search Algorithm
# ---------------------------------------------------------------------------------

# ------------------------------ Iterative Solution ------------------------------
#
#
#
# Time Complexity : O(log n)
#
# Space Complexity : O(1) Constant
# ----------------------------------------------------------------------------------

def binary_search_iterative(arr: list[int], item : int)-> int:
    high : int  = len(arr)-1
    low : int = 0
    result : int =0

    while high>=low:
        mid : int = high+low//2
        if item == arr[mid] : 
            result = mid
            break
        elif item > arr[mid]:
            low = mid+1
        else :
            high = mid-1

    return result


# ------------------------------ Recursive Solution ------------------------------
#
#
#
# Time Complexity : O(log n)
#
# Space Complexity : O(1) Constant
# ----------------------------------------------------------------------------------


def binary_search_recursive(arr : list[int], high:int , low:int, item : int)-> int:
    mid_point : int = high+low//2
    
    if (low<high):
        if item == arr[mid_point]:
            return mid_point
        elif item > arr[mid_point]:
            return binary_search_recursive(arr, high , mid_point+1, item)
        else:
            return binary_search_recursive(arr, mid_point-1, low,item)
    else:
        return -1


# Driver Code
def main():
    input_1 : list[int] = [2, 3, 6, 12, 15, 18]

    result_1 = binary_search_recursive(input_1, len(input_1)-1,0,6)
    print_result(result_1)

    result_2 = binary_search_iterative(input_1,6)
    print_result(result_2)




# Helper function - can be ignored
def print_result(result:int):
    if result== -1:
        print("Not Found")
    else:
        print("Found at index : " +str(result))

main()
