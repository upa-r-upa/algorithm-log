class MyCircularQueue:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.queue = [None] * k

        self.MAX_SIZE = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.MAX_SIZE

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.MAX_SIZE

        return True

    def Front(self) -> int:
        if self.queue[self.front] == None:
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.queue[self.rear - 1 % self.MAX_SIZE] == None:
            return -1

        return self.queue[self.rear - 1 % self.MAX_SIZE]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.Front() == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.Rear() != -1:
            return True
        else:
            return False
