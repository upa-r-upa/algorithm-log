import sys

k = int(sys.stdin.readline().rstrip())
stack = []
for i in range(k):
    cmd = int(sys.stdin.readline().rstrip())

    if cmd == 0:
        stack.pop()
    else:
        stack.append(cmd)
        
print(sum(stack))