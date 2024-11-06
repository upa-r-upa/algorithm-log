# 1. deque 버전
from collections import deque
import sys

readline = sys.stdin.readline

class queue():
    def __init__(self):
        self.q = deque()
    
    def size(self) -> int:
        return len(self.q)

    def empty(self) -> int:
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self) -> int:
        if self.empty():
            return -1

        return self.q[0]
        
    def back(self) -> int:
        if self.empty():
            return -1

        return self.q[-1]

    def push(self, x):
        return self.q.append(x)

    def pop(self) -> int | None:
        if self.empty():
            return -1

        return self.q.popleft()

def solution():
    q = queue()
    n = int(readline().rstrip())

    for i in range(n):
        command = readline().rstrip()

        if command.startswith("push"):
            _, x = command.split()

            q.push(int(x))
        elif command == "pop":
            print(q.pop())
        elif command == "size":
            print(q.size())
        elif command == "empty":
            print(q.empty())
        elif command == "front":
            print(q.front())
        elif command == "back":
            print(q.back())
        else:
            raise Exception("Not a valid command")

solution()