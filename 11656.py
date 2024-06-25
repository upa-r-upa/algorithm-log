import sys

def selection_sort(arr):
	for i in range(len(arr)):
		min_idx=i
		
		for j in range(i,len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx=j
		
		arr[i],arr[min_idx]=arr[min_idx],arr[i]
		
	return arr

s=sys.stdin.readline().rstrip()
result=[]

for i in range(len(s)):
	result.append(s[i:])
	
print(*selection_sort(result),sep="\n")