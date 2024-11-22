from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    
    directions=[(-1,0), (1,0), (0, -1), (0, 1)] # 위,아래,왼쪽,오른쪽
    
    def check_moveable(row, col):
        return row < n and row >= 0 and col < m and col >= 0
    
    def bfs():
        queue = deque([((0,0), 1)]) # (row, col), distance
        maps[0][0] = 0
        
        while queue:
            [row, col], distance = queue.popleft()
            
            if row+1 == n and col+1 == m:
                return distance
            
            move_end = True
            
            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                
                if check_moveable(next_row, next_col) and maps[next_row][next_col] == 1:
                    queue.append(((next_row, next_col), distance + 1))
                    maps[next_row][next_col] = 0
                    
                    move_end=False # 갈 곳이 있으면 위로 이동 안함
                
            if move_end:
                # 다만 큐가 남아있다면 끝이 아님. 이 길이 막힌 것
                if not queue:
                    return -1
                else:
                    continue
    return bfs()