from copy import copy

class Queue:
    def __init__(self) -> None:
        self._arr = []
        self._size = len(self._arr)
        self._front = self._size-1
        self._back = 0


    def enqueue(self,val) -> None:
        # insert an item at back of the array
        self._arr.insert(self._back,val)
        self._recalc()

    def dequeue(self):
        result = copy(self._arr[self._front])
        self._arr.pop(self._front)
        self._recalc()
        return result

    @property
    def size(self) -> int:
        return self._size

    def top(self):
        return self._arr[self._front]


    def _recalc(self) -> None:
        self._back = 0
        self._size = len(self._arr)
        self._front = self._size-1


    def __str__(self) -> str:
        display_str = "["

        for item in self._arr[::-1]:
            display_str += str(item) + " , "

        return display_str + "]"
        