def solution(array, commands):
    result = []
    
    for command in commands:    
        [i, j, k] = command
        
        sliced_array = array[i-1:j]
        k_num = _sorted(sliced_array)[k-1]
        
        result.append(k_num)
    
    return result

def _sorted(array):
    return quick_sorted(array)

def insert_sorted(array):
    for i in range(1, len(array)):
        curr = array[i]
        j = i - 1
        
        while j >= 0 and curr < array[j]:
            array[j+1] = array[j]
            j = j-1
            
        array[j+1] = curr
        
    return array

def quick_sorted(array):
    if len(array) < 2:
        return array
    
    pivot = array[len(array)//2]
    
    left=[x for x in array if x < pivot]
    mid=[x for x in array if x == pivot]
    right=[x for x in array if x > pivot]
    
    return quick_sorted(left) + mid + quick_sorted(right)
            

def merge_sorted(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sorted(array[:mid])
    right = merge_sorted(array[mid:])
    
    left_idx = 0
    right_idx = 0
    
    result = []
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
            
    result += left[left_idx:]
    result += right[right_idx:]
            
    return result
    