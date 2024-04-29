def solution(emergency):
    result = merge_sort(emergency)
    return [result.index(v) + 1 for v in emergency]
    

def merge_sort_compare(arr1, arr2):
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
    
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge_sort_compare(left, right)