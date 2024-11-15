import sys
from collections import deque

graph = dict()
visited = set()
dfs_result = []

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    dfs_result.append(node)

    for neighbor in graph[node]:
        dfs(neighbor)

def bfs(start_node):
    bfs_result = []
    q = deque([start_node])
    visited_bfs = set([start_node])

    while q:
        node = q.popleft()
        bfs_result.append(node) 
    
        for neighbor in graph[node]:
            if neighbor not in visited_bfs:
                q.append(neighbor)
                visited_bfs.add(neighbor)

    return bfs_result


input = sys.stdin.readline

n,m,v = map(int, input().rstrip().split())

for i in range(n):
    graph[i+1] = []

for _ in range(m):
    a,b = map(int, input().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)

for nodes in graph.values():
    nodes.sort()

dfs(v)

print(*dfs_result, sep=" ")
print(*bfs(v), sep=" ")