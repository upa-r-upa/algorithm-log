n, k = map(int, input().split())
n_l = list(map(int, [input() for i in range(n)]))

c = 0

for v in n_l[::-1]:
    if v <= k:
        c = c + k // v
        k = k - (k // v) * v

        if k <= 0:
            break
			
print(c)