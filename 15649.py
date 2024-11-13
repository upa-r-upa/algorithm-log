from itertools import permutations


n, m = map(int, input().split())
items = list(range(1, n + 1))

perms = permutations(items, m)

for perm in perms:
    print(' '.join(map(str, perm)))