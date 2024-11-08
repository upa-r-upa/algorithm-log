import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def solution_1():
    class MinHeap:
        def __init__(self):
            self.q = [-1]

        def push(self, item):
            if len(self.q) == 1:
                return self.q.append(item)

            i = len(self.q)
            self.q.append(item)

            while i > 1 and self.q[i//2] > item:
                self.q[i] = self.q[i//2]
                self.q[i//2] = item
                i = i//2

            return item

        def pop(self):
            if len(self.q) == 1:
                return 0

            value = self.q[1]
            last_value = self.q.pop()

            if len(self.q) == 1:
                return value
            
            i = 1
            self.q[i] = last_value

            while i*2 < len(self.q) and (self.q[i*2] < last_value or (i*2+1 < len(self.q) and self.q[i*2+1] < last_value)) :
                left=i*2
                right=i*2+1

                if len(self.q) <= right or self.q[left] < self.q[right]:
                    self.q[i] = self.q[left]
                    self.q[left] = last_value
                    i=left
                else:
                    self.q[i] = self.q[right]
                    self.q[right] = last_value
                    i=right

            return value
            

    n = int(input().rstrip())
    heap = MinHeap()

    for _ in range(n):
        x = int(input().rstrip())

        if x == 0:
            print(heap.pop())
        else:
            heap.push(x)

def solution_2():
    n=int(input().rstrip())
    heap = []

    for _ in range(n):
        x=int(input().rstrip())

        if x == 0:
            print(0 if not heap else heappop(heap))
        else:
            heappush(heap, x)

solution_2()