n = int(input())
result = [int(input()) for i in range(n)]

for i in range(1, n):
	value = result[i]
	j = i

	while j > 0 and result[j-1] > value:
		result[j] = result[j-1]
		j -= 1
	
	result[j] = value

print(*result, sep="\n")