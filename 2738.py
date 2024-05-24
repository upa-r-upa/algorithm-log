from sys import stdin
n,m=map(int, stdin.readline().rstrip().split())
result=[list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    matrix=list(map(int, stdin.readline().rstrip().split()))
    
    for j in range(m):
        result[i][j] += matrix[j]

for string in result:
    print(*string)