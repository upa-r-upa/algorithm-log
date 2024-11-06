n,k = map(int, input().split())
people = [i+1 for i in range(n)]
result = []
curr_index = 0

while people:
	index = (curr_index + k - 1) % len(people)
	result.append(people.pop(index))

	curr_index = index

print("<", end="")
print(*result, sep=", ", end="")
print(">")
