class MyCircularDeque:
    def __init__(self, k: int):
        # Initialize your data structure here. Set the size of the deque to be k.
        self._size = k
        self._count = 0
        self._head = self._tail = 0
        self._data = [-1] * k

    def insertFront(self, value: int) -> bool:
        # Adds an item at the front of Deque. Return true if the operation is successful.
        if self.isFull(): return False
        if self.isEmpty(): 
            self._data[self._head] = value
        else:
            self._head = (self._head - 1) % self._size
            self._data[self._head] = value
        self._count += 1
        return True

    def insertLast(self, value: int) -> bool:
        # Adds an item at the rear of Deque. Return true if the operation is successful.
        if self.isFull(): return False
        if self.isEmpty(): 
            self._data[self._tail] = value
        else:
            self._tail = (self._tail + 1) % self._size
            self._data[self._tail] = value
        self._count += 1
        return True

    def deleteFront(self) -> bool:
        # Deletes an item from the front of Deque. Return true if the operation is successful.
        if self.isEmpty(): return False
        self._data[self._head] = -1
        self._head = (self._head + 1) % self._size
        self._count -= 1
        if self._count == 0: # 删除最后一个元素的时候，head会多向右移动一格，此时head!=tail
            self._tail = self._head 
        return True

    def deleteLast(self) -> bool:
        # Deletes an item from the rear of Deque. Return true if the operation is successful.
        if self.isEmpty(): return False
        self._data[self._tail] = -1
        self._tail = (self._tail - 1) % self._size
        self._count -= 1
        if self._count == 0: # 删除最后一个元素的时候，tail会多向左移动一格，此时head!=tail
            self._head = self._tail
        return True

    def getFront(self) -> int:
        # Get the front item from the deque.
        return self._data[self._head]

    def getRear(self) -> int:
        # Get the last item from the deque.
        return self._data[self._tail]

    def isEmpty(self) -> bool:
        # Checks whether the circular deque is empty or not.
        return False if self._count else True

    def isFull(self) -> bool:
        # Checks whether the circular deque is full or not.
        return self._count == self._size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()