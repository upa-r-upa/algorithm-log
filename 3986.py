import sys

n = int(sys.stdin.readline().rstrip())
count = 0

for i in range(n):
	stack = []
	strings = sys.stdin.readline().rstrip()
	
	if len(strings) % 2 != 0:
		continue
		
	for value in strings:
		if len(stack) > 0 and stack[len(stack)-1] == value:
			stack.pop()
		else:
			stack.append(value)
			
	if len(stack) == 0:
		count += 1
		
print(count)