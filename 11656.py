import sys

def insertion_sort(arr):
	for i in range(1,len(arr)):
		curr = arr[i]
		j = i-1
		
		while j >= 0 and arr[j] > curr:
			arr[j+1] = arr[j]
			j -= 1
		
		arr[j+1] = curr
	
	return arr
			
			
s=sys.stdin.readline().rstrip()
result=[]

for i in range(len(s)):
	result.append(s[i:])
	
print(*insertion_sort(result),sep="\n")