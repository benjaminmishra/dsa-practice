# ------------------------------- Problem ----------------------
# Given an array, write a program to generate a random permutation of array elements. 
# This question is also asked as “shuffle a deck of cards” or “randomize a given array”. 
# Here shuffle means that every permutation of array element should equally likely.

# Example :
# Input arr = [1,2,3,4,5,6,7,8]
# Result arr = [7,8,4,6,3,1,2,5]
# The output can be any random permutation of the of the input array such that the 
# probablity of getting the output is 1/n if n is the size of the input array.
# -------------------------------------------------------------------------------


# ------------------------------- Simple Solution-----------------------------
# Lets say the input array is called arr
# Follwow the follwing steps
# (1) Copy the input array arr and name the copy as arr_copy
# (2) Randomly select an number which is and pick that item from arr_copy 
# (3) 