def solution(strArr):
    result = dict()
    
    for i in strArr:
        result[len(i)] = result.get(len(i), 0) + 1
            
    return max(result.values())