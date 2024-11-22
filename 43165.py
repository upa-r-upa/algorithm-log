# DFS
def solution_dfs(numbers, target):
    count = 0
    
    def dfs(idx, total):
        nonlocal count
        
        if idx == len(numbers):
            if total == target:
                count += 1
            return
        
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
        
    dfs(0,0)
    
    return count

# BFS
from collections import deque

def solution_bfs(numbers, target):
    count = 0
    
    def dfs():
        queue = deque([(0,0)])
        nonlocal count
        
        while queue:
            idx, total = queue.popleft()
            
            if idx == len(numbers):
                if total == target:
                    count += 1
                    
                continue
        
            queue.append((idx + 1, total + numbers[idx]))
            queue.append((idx + 1, total - numbers[idx]))
        
    dfs()
    
    return count