# ----------------------------------------------------------------
# Convert an infix expression to a postfix or reverse ploish notation expression
# Usage             Infix -> Postfix -> Operate on postfix 
# -----------------------------------------------------------------



# --------------------- Solution O(n) - Linear time -----------------------
# Also known as the Shunting yard Algorithm
# The algorithm uses a stack and a queue for achieve its objective
# Rules for the algorithm

# (1) Operator goes into the stack (i.e. add substract div etc)
# (2) While pushing operator into stack check if there is an operator already on the top of the stack with higher or equal precedance
# (3) If yes pop it and keep poping it until all higher or same precedance operators are poped
# (4) Operands go into the queue (numbers on which the operator operates on)
# (5) Starting brackets go into the stack , same as operators
# (6) When encountered with a closing bracket keep poping items from stack until you reach an opening bracket

# Precedance of Operators 
#  ^ > / > * > + > -    (BODMAS rule)
#
# ---------------------------------------------------------------------------