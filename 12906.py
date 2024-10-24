def solution(arr):
    result = []
    
    for num in arr:
        if len(result) == 0 or result[-1] != num:
            result.append(num)
    
    return result