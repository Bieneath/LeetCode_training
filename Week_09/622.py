class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [None] * k
        self.front = self.rear = 0
        self.size = 0
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False
        if not self.isEmpty():
            self.rear = (self.rear + 1) % self.max_size
        self.data[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.size > 1:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size