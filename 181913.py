def solution(my_string, queries):
    result=list(my_string)
    
    for start, end in queries:
        result[start:end+1] = result[start:end+1][::-1]
        
    return "".join(result)