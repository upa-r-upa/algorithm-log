import sys
from itertools import permutations

input = sys.stdin.readline
n=int(input().rstrip())
arr = [i+1 for i in range(n)]

for num in permutations(arr, n):
    print(*num)