import sys
n=int(sys.stdin.readline().rstrip())
a=list(map(int, sys.stdin.readline().rstrip().split()))
count = {}
stack = [0]
result = [-1] * n

for i in range(n):
	if a[i] in count:
		count[a[i]] += 1
	else:
		count[a[i]] = 1

for i in range(1,n):
	while stack and count[a[stack[-1]]] < count[a[i]]:
		result[stack.pop()] = a[i]
	
	stack.append(i)
	
print(*result)