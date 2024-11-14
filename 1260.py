import sys

graph = dict()
visited = set()
result = []

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        dfs(neighbor)

input = sys.stdin.readline

n,m,v = map(int, input().rstrip().split())

for _ in range(m):
    a,b = map(int, input().rstrip().split())
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

print(graph)
dfs(v)

print(result)