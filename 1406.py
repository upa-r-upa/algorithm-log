import sys

left = list(sys.stdin.readline().rstrip())
right = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
	command = sys.stdin.readline().rstrip()
	
	if command == "L":
		if left:
			right.append(left.pop())
	elif command == "D":
		if right:
			left.append(right.pop())
	elif command == "B":
		if left:
			left.pop()
	else:
		left.append(command[2])
		
	
print("".join(left), end="")
print("".join(reversed(right)))