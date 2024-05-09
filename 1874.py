import sys

t = int(sys.stdin.readline().rstrip())

curr = 1
stack = [1]
ans = "+"

for i in range(t):
	n = int(sys.stdin.readline().rstrip())

	if ans == "NO": continue
	
	if (len(stack) == 0 or (stack[len(stack)-1] < n)) and curr < n:
		stack.extend(list(range(curr+1, n)))
		ans += "+" * (n - curr)
		ans += "-"

		curr = n
	elif len(stack) > 0 and stack[len(stack)-1] == n:
		stack.pop()
		ans += "-"
	elif len(stack) > 0 and stack[len(stack)-1] > n and n in stack:
		idx = stack.index(n) 
		ans += "-" * (len(stack)-idx) 
		stack = stack[:idx]
	else:
		ans = "NO"

if ans == "NO":
	print("NO")
else:
	print(*ans, sep="\n")