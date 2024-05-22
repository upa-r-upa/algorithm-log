from sys import stdin

n,m = map(int, input().split())
baskets = [i for i in range(1,n+1)]

for _ in range(m):
    i,j = map(int, stdin.readline().rstrip().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]
print(*baskets)