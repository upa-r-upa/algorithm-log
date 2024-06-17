n, k = map(int, input().split())
idx = 0
people = [i for i in range(1, n+1)]
result = []

while people:
	next_idx = (idx + k - 1) % len(people)
	result.append(people.pop(next_idx))
	idx = next_idx

print("<" + ", ".join(map(str, result)) + ">")