import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

def get_worm_count():
    count = 0
    m,n,k = map(int, input().rstrip().split())
    positions = [(-1, 0), (1, 0), (0,-1), (0,1)]

    graph = [[0] * m for _ in range(n)]

    def search(is_dfs, row, col):
        if is_dfs:
            dfs(row, col)
        else:
            bfs(row, col)

    def dfs(row, col):
        graph[row][col] = 0

        for pos_row, pos_col in positions:
            nr = row+pos_row
            nc = col+pos_col

            if nr >= 0 and nc >= 0 and nr < n and nc < m and graph[nr][nc] == 1:
                dfs(nr, nc)

    def bfs(row, col):
        graph[row][col] = 0
        queue = deque([(row, col)])

        while queue:
            row,col = queue.popleft()

            for pos_row, pos_col in positions:
                nr = row+pos_row
                nc = col+pos_col
                
                if nr >= 0 and nr < n and nc >= 0 and nc < m and graph[nr][nc] == 1:
                    queue.append((nr, nc))
                    graph[nr][nc] = 0
                
    for _ in range(k):
        col,row = map(int, input().rstrip().split())

        graph[row][col] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                search(False, i, j)
                count += 1

    return count



for _ in range(t):
    print(get_worm_count())