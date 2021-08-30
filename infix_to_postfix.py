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
from linear_ds import Stack, Queue

def infix_to_postfix(infix_str:str) -> Queue:
    s : Stack = Stack()
    q : Queue = Queue()

    prec : dict = {
        "^" : 4,
        "/" : 3,
        "*" : 2,
        "+" : 1,
        "-" : 0
    }

    for item in infix_str.split():
        if item.isdigit():
            q.enqueue(item)
        elif item == ")":
            while not s.is_empty() and not s.top() == "(" :
                q.enqueue(s.pop())
            
            if not s.is_empty() and s.top()=="(": 
                s.pop()
        else:
            while not s.is_empty() and not item == "(" :
                if not s.top() == "(" and prec[s.top()] > prec[item]:
                    q.enqueue(s.pop())
                else:
                    break

            s.push(item)

    while not s.is_empty():
            q.enqueue(s.pop())

    return q



def main():
    input_1 : str = "3 * ( 4 + 5 )"
    result_1 : Queue = infix_to_postfix(input_1)
    print(result_1)

    input_2 : str = "3 * 4 + 5"
    result_2 : Queue = infix_to_postfix(input_2)
    print(result_2)


main()
