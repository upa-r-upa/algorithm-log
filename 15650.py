
from itertools import combinations

n,m = map(int, input().rstrip().split())
numbers = [i+1 for i in range(n)]

combination = combinations(numbers, m)

for combi in combination:
    print(*combi)