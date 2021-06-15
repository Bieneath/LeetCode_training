class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [None] * k
        self.count = 0
        self.k = k
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if not self.isEmpty():
            self.rear = (self.rear + 1) % self.k
        self.data[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.count > 1:
            self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k