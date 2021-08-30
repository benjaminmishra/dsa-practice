# Stack implementation in python, LIFO data strruct using list comprehension
from copy import copy

class Stack:
    def __init__(self) -> None:
        self._arr : list[any] = []
        self._calc_size_top()

    def push(self, val) -> None:
        '''adds item to the top of the stack'''
        self._arr.append(val)
        self._calc_size_top()

    def pop(self):
        '''removes item from top of stack and returns it'''
        to_be_popped = copy(self._arr[self._top_idx])
        self._arr.pop()
        self._calc_size_top()
        return to_be_popped

    def top(self):
        '''gets the top item from the stack without removing it'''
        return self._arr[self._top_idx]

    @property
    def size(self) -> int:
        '''readonly property that gets the size of the current stack'''
        return self._size

    def is_empty(self) -> bool:
        self._calc_size_top()
        if self._size == 0:
            return True
        else:
            return False 


    def _calc_size_top(self) -> None:
        '''private function to recalculate the properties inside stack object'''
        self._size = len(self._arr)
        self._top_idx = self._size-1

    def __str__(self) -> str:
        display_str = "["

        for item in self._arr:
            display_str += str(item) + " , "

        return display_str + "]"