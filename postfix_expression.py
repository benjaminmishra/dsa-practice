# ------------------------------- Problem Description ----------------------------
# Evaluate the value of an arithmetic expression in Reverse Polish Notation also know as postfix notation.
# 
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
#
# Note that division between two integers should truncate toward zero.
# It is guaranteed that the given RPN expression is always valid. 
# That means the expression would always evaluate to a result, and there will not be any division by zero operation.
#
# 2 1 + 3 *
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# ---------------------------------------------------------------------------------




# ----------------------------- Using Stack O(n) linear time --------------------------------
# This needs to be solved using stack, the algo as following
# Start evaluating from beginning of the string
# Everytime we encounter an operand i.e. numbers or variables we push it onto stack
# Everytime we encounter an operator i.e. + , - , * , / , ^ we pop top two items from the stack
# and perfrom the operation on the numbers and push the result back into the stack
#
# We keep repeating the above steps until we reach the end of the expression 
# After which we will be left with the result of the expression

# Time Complexity: Linear time O(n) as we use only one for loop and make one pass of the input
#
# Space Complexity: O(n) , because at most we can have all the operands in the stack at any given time
#------------------------------------------------------------------------------------

from linear_ds import Stack
import operator

def postfix_eval(postfix_expression : str) -> int:
    # initialize an empty stack
    stack :Stack = Stack()

    # create an expression / operator dict
    operator_dict : dict= {
        "+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
        "/":operator.truediv,
        "^":operator.pow
    }

    # Split the input expression based on white spaces and loop on the resulting array
    for item in postfix_expression.split():
        # Check if the item we are on is a digit, if yes push it in stack otherwise its an operator
        if item.isdigit():
            stack.push(item)
        else:
            # pop  items from stack and operate on them
            operand_1 : int = int(stack.pop())
            operand_2 : int = int(stack.pop())

            # push back the result to stack
            stack.push(operator_dict[item](operand_1, operand_2))

    # at the end find the last item in the stack , that should be ans
    return stack.top()



# Driver Code

def main():
    postfix_input_1 = "2 1 + 3 *"
    result_1 = postfix_eval(postfix_input_1)
    print(result_1)

    postfix_input_2 = "4 5 - 6 7 + 8 9 8 * -"
    result_2= postfix_eval(postfix_input_2)
    print(result_2)

    postfix_input_3 = "10 2 8 * + 3 -"
    result_3= postfix_eval(postfix_input_3)
    print(result_3)


main()
