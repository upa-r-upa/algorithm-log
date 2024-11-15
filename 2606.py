import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():

    n = int(input())
    edges = int(input())

    graph = dict()
    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                
    for i in range(n):
        graph[i+1] = []
    
    for j in range(edges):
        a,b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
    
    dfs(1)

    return len(visited) - 1



print(solve())