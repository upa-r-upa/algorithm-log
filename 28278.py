import sys

n = int(input())
stack = []

for _ in range(n):
	cmd = sys.stdin.readline().rstrip()
	
	match cmd:
		case "2":
			if len(stack) > 0:
				print(stack.pop())
			else:
				print("-1")
		case "3":
			print(len(stack))
		case "4":
			print(int(len(stack) == 0))
		case "5":
			if len(stack) > 0:
				print(stack[len(stack) - 1])
			else:
				print("-1")
		case _:
			stack.append(cmd.split()[1])
			
