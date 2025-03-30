N = int(input())

total = 0

for _ in range(N):
    S, A = map(int, input().split())
    per = A // S
    left = A % S
    total += left

print(total)