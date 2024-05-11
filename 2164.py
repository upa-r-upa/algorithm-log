n = int(input())
queue = [i for i in range(1,n+1)]
idx = 0

while len(queue) - 1 > idx + 1:
	idx += 1

	if len(queue) - 1 > idx + 2:
		queue.append(queue[idx])
		idx += 1

print(queue[len(queue)-1])