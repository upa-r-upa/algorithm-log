import sys

n = int(input())
queue = []

for i in range(n):
	cmd = sys.stdin.readline().rstrip()
	
	match cmd:
		case "pop":
			if len(queue) == 0:
				print("-1")
			else:
				print(queue[0])
				queue = queue[1:]
		case "size":
			print(len(queue))
		case "empty":
			print(int(len(queue) == 0))
		case "front":
			if len(queue) == 0:
				print("-1")
			else:
				print(queue[0])
		case "back":
			if len(queue) == 0:
				print("-1")
			else:
				print(queue[len(queue) - 1])
		case _:
			queue.append(int(cmd.split(" ")[1]))