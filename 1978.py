import sys
import math

input=sys.stdin.readline


n=int(input().rstrip())
nums=list(map(int,input().rstrip().split()))
count=0

def is_prime(n):
    if n == 1:
        return False
        
    num=int(math.sqrt(n))
    for j in range(2, num+1):
        if n % j == 0:
            return False
    return True

for i in range(n):
    count += 1 if is_prime(nums[i]) else 0

print(count)