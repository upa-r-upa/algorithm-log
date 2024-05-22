import sys
input_sys = sys.stdin.readline

x = int(input_sys().rstrip())
n = int(input_sys().rstrip())

for i in range(n):
    a,b=input_sys().rstrip().split()
    x -= int(a)*int(b)

print("No" if x != 0 else "Yes")