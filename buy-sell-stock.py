# ------------------------------- Problem Description ----------------------------
#
#
# ---------------------------------------------------------------------------------



# ------------------------------ Brute Force Solution O(n^2)------------------------------
# The appraoch is simple, it compares every price with every other price to find the diffrence between them
# Everytime it finds a new maximum it overwrites the old maximum. However, for this to happen every 
# element needs to be compared to every other element. Making this approach inefficient.
# Time Complexity : O(n^2) , because there are two nested for loops here
# Space Complexity : O(1) , constant because we just use three addtional variables,
#                           to keep track of buy sell and max profit at any given time.
# ----------------------------------------------------------------------------------

def find_max_profit_slow(prices : list[int])->int:
    # variables to keep track of some things, optional except the max profit
    buy : int = 0
    sell :int = 0
    max_profit: int = 0

    # loop through every price with every other price
    # hence we need nested for loops
    for i in range(0,len(prices)):
        buy = prices[i]
        for j in range(i,len(prices)):
            sell = prices[j]

            # find max profit only when buy is greater than sell
            if buy<sell:
                profit : int = sell-buy
                # compare with current profit with the last max profit
                # overwrite max profit only when we find a new max profit. 
                max_profit = max(profit, max_profit)
    
    return max_profit

    



# ----------------------------- Efficient Solution  O(n)--------------------------------
# variation of Kaden's algo. All we need to do here is go to each price in the given array, 
# and for each position see what is the least price seen so far (i.e. till that postion of the array).
# Once we know that what is the minimum seen so far, we find the difference of the current price with the 
# minumum seen so far. This becomes the current maximum profit. Then we compare this current maximum profit
# with the global maximum so far. Which ever is greater, we take that. At the end of the array the 
# max profit value becomes the max profit that can be made.
#
# Time Complexity: O(n) , this only requires a single pass of the array
#
# Space Complexity: O(1) , constant since we barely store anything extra.
#------------------------------------------------------------------------------------

def find_max_profit_efficient(prices : list[int])->int:
    max_profit = float("-inf")
    min_price_so_far : int = prices[0]

    for i in range(1,len(prices)):
        min_price_so_far= min(min_price_so_far, prices[i])
        profit = prices[i] - min_price_so_far
        max_profit = max(profit, max_profit)
    
    return max_profit



# Driver Code

def main():
    input_1 : list[int] = [310,315,275,295,260,270,290,230,255,250,800,500,345,890,455,555,500,600,675,680,690]
    result_1 : int = find_max_profit_slow(input_1)
    result_2 : int = find_max_profit_efficient(input_1)
    
    print("Slow method :" + str(result_1))
    print("Fast Method :" + str(result_2))

    input_2 : list[int] = [310,315,275,295,260,270,290,230,255,250]
    result_3 : int = find_max_profit_slow(input_2)
    result_4 : int = find_max_profit_efficient(input_2)
    
    print("Slow method :" + str(result_3))
    print("Fast Method :" + str(result_4))

    

main()
