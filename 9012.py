import sys
n = int(input())

for _ in range(n):
	cmd = sys.stdin.readline().rstrip()
	stack = []
	
	if len(cmd) % 2 != 0:
		print("NO")
		continue
	
	for s in cmd:
		if len(stack) > 0 and stack[len(stack)-1] == "(" and s == ")":
			stack.pop()
		else:
			stack.append(s)
		
	if len(stack) > 0:
		print("NO")
		continue
		
	print("YES")