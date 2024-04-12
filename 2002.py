import sys

n = int(input())
count = 0

origin = [sys.stdin.readline().rstrip() for i in range(n)]

for i in range(n):
    s = sys.stdin.readline().rstrip()

    if origin[i - count] != s:
        count += 1
        origin.remove(s)

print(count)