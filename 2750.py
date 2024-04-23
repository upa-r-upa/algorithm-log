def merge_sort_inner(arr1, arr2):
	i = j = 0
	result = []
	
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1

	result.extend(arr1[i:])
	result.extend(arr2[j:])

	return result

def merge_sort(array):
	if len(array) <= 1: 
		return array

	mid = len(array) // 2

	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])

	return merge_sort_inner(left, right)

n = int(input())
arr = [int(input()) for i in range(n)]
print(*merge_sort(arr), sep="\n")