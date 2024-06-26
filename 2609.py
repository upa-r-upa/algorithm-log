import sys
x,y=map(int, sys.stdin.readline().rstrip().split())

def gcd(a,b):
    while b > 0:
        a,b=b,a%b

    return a

print(gcd(x,y))
print(x*y//gcd(x,y))