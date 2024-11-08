import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        print(0 if not heap else heappop(heap)[1])
    else:
        heappush(heap, (abs(x),x))