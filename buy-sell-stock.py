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

    



# ----------------------------- Effiecient Solution --------------------------------
#
#
#
# Time Complexity:
#
# Space Complexity:
#------------------------------------------------------------------------------------

def function_name_efficient():
    pass



# Driver Code

def main():
    input_1 : list[int] = [310,315,275,295,260,270,290,230,255,250,800,500,345,890,455, 555,500,600,675,680,690]
    result_1 : int = find_max_profit_slow(input_1)
    print(result_1)


main()
