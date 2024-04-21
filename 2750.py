def swap(array, idx_a, idx_b):
	temp = array[idx_a]
	array[idx_a] = array[idx_b]
	array[idx_b] = temp

n = int(input())
result = [int(input()) for i in range(n)]

for i in range(n):
	for idx in range(n-i-1):
		if result[idx] > result[idx + 1]:
			swap(result, idx, idx + 1)
	
print(*result, sep="\n")