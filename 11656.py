import sys

def merge_sort(arr):
	if len(arr) == 1:
		return arr
		
	pivot=len(arr)//2
	
	left=merge_sort(arr[:pivot])
	right=merge_sort(arr[pivot:])
	
	return merge_arr(left,right)

def merge_arr(left,right):
	result = []
	
	i=j=0
	
	while len(left) > i and len(right) > j:
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	while i < len(left):
		result.append(left[i])
		i+=1
	while j < len(right):
		result.append(right[j])
		j+=1
	return result
    
s=sys.stdin.readline().rstrip()
result=[]

for i in range(len(s)):
	result.append(s[i:])
	
print(*selection_sort(result),sep="\n")