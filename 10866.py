import sys

read = sys.stdin.readline
n = int(read().rstrip())

arr = []

for _ in range(n):
	cmd = read().rstrip()
	
	if cmd == "pop_front":
		print(arr.pop(0) if arr else -1)
	elif cmd == "pop_back":
		print(arr.pop() if arr else -1)
	elif cmd == "size":
		print(len(arr))
	elif cmd == "empty":
		print(int(len(arr) == 0))
	elif cmd == "front":
		print(arr[0] if arr else -1)
	elif cmd == "back":
		print(arr[-1] if arr else -1)
	elif cmd.startswith("push_front"):
		arr.insert(0, int(cmd.split()[-1]))
	elif cmd.startswith("push_back"):
		arr.append(int(cmd.split()[-1]))