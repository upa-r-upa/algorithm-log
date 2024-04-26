import sys

n = int(sys.stdin.readline().rstrip())
array = []

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command == "pop":
        if len(array) > 0: print(array.pop())
        else: print(-1)
    elif command == "size":
        print(len(array))
    elif command == "empty":
        print(int(len(array) == 0))
    elif command == "top":
        if len(array) > 0: print(array[len(array)-1])
        else: print(-1)
    else:
        array.append(int(command.split()[1]))
	