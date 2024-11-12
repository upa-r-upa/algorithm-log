import sys
from heapq import heappushpop, heappush

input = sys.stdin.readline

n = int(input().rstrip())
min_heap = []

for _ in range(n):
    row = map(int, input().strip().split())

    for num in row:
        if len(min_heap) < n:
            heappush(min_heap, num)
        elif min_heap[0] < num:
            heappushpop(min_heap, num)

print(min_heap[0])

# n개만 저장해야 할 것 같다. (왜냐면 n번째 큰 수니까)
# 그럼 가장 최대 힙으로 저장해야 할까?
# 근데 heap은 가장 작은 값이 맨 뒤에 있다는 가정이 없음 .
# 그렇다고 최대힙인데 왼쪽을 뽑을 순 없음.
# 그럼 최소 힙으로 저장하면? (pop하면 가장 큰 값이 뒤로 감)
# 그럼 최소 힙으로 저장하고, 

# 가장 작은 값을 계속 빼내면? 근데 이러면 안됨.
# 항상 n개를 유지하면서 넣었다 빼야 함.-> 그럼 n번째인걸 확정할 수 있는지?
# -> 0번째가 n번째 큰 값이 됨
# 12 > 9 
# [10,10,12,13,14,15]
# [10,12,13,14,15]