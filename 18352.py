from collections import deque
from sys import stdin

def input():
    return stdin.readline().rstrip()

def solve():
    n,m,k,x=map(int, input().split())
    graph = {}
    distance = {}

    for i in range(n):
        graph[i+1] = []
        distance[i+1] = -1

    for _ in range(m):
        a,b = map(int, input().split())

        graph[a].append(b)
    
    def bfs(start_node):
        distance[start_node] = 0
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            
            if distance[node] == k:
                break
            
            for neighbor in graph[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node]+1
                    queue.append(neighbor)

    bfs(x)

    result = []

    for key in distance.keys():
        if distance[key] == k:
            result.append(key)

    return result if result else [-1]

print(*solve(), sep="\n")