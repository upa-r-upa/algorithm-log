import sys
from collections import deque

read = sys.stdin.readline
n=int(read().rstrip())

arr = deque()

for _ in range(n):
	cmd = read().rstrip()
	
	if cmd == "pop_front":
		print(arr.popleft() if arr else -1)
	elif cmd == "pop_back":
		print(arr.pop() if arr else -1)
	elif cmd == "size":
		print(len(arr))
	elif cmd == "empty":
		print(int(len(arr) == 0))
	elif cmd == "front":
		if arr:
			front=arr.popleft()
			arr.appendleft(front)
			print(front)
		else:
			print(-1)
	elif cmd == "back":
		if arr:
			back=arr.pop()
			arr.append(back)
			print(back)
		else:
			print(-1)
	elif cmd.startswith("push_front"):
		arr.appendleft(int(cmd.split()[-1]))
	elif cmd.startswith("push_back"):
		arr.append(int(cmd.split()[-1]))