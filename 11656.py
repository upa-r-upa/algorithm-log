import sys

def quick_sort(arr):
    def partition(arr, start, end) -> int:
        pivot = arr[(start+end)//2]
        
        while start <= end:
            while arr[start] < pivot:
                start += 1
            while arr[end] > pivot:
                end -= 1
            if start<=end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        return start
        
    def sort(arr, start, end):
        if end <= start:
            return arr
            
        pivot = partition(arr, start, end)
        
        sort(arr, start, pivot-1)
        sort(arr, pivot, end)
        
        return arr
    
    return sort(arr, 0, len(arr)-1)

s=sys.stdin.readline().rstrip()
result=[]

for i in range(len(s)):
	result.append(s[i:])
	
print(*quick_sort(result),sep="\n")