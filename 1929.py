import sys
import math

input=sys.stdin.readline


m,n=list(map(int,input().rstrip().split()))
nums=[i for i in range(m,n+1)]

def is_prime(n):
    if n == 1:
        return False
        
    num=int(math.sqrt(n))
    for j in range(2, num+1):
        if n % j == 0:
            return False
    return True

for i in range(len(nums)):
    if is_prime(nums[i]):
        print(nums[i])