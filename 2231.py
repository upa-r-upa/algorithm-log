n=int(input())
result = 0
for i in range(1,n):
	arr_i = list(map(int, str(i)))

	if sum(arr_i) + i == n:
		result = i
		break
		
print(result)