from sys import stdin

n,m = map(int, input().split())
baskets = [0] * n

for i in range(m):
    i,j,k = map(int, stdin.readline().rstrip().split())
    baskets[i-1:j] = [k] * (j-i + 1)

print(*baskets)