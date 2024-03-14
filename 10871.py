n, x = map(int, input().split())
a = list(map(int, input().split()))
r = []

for i in range(n):
    if a[i] < x:
        r.append(str(a[i]))

print(*r)