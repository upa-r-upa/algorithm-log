def solution(s):
    result = set([len(s)])
    for i in range(1,len(s)):
        result.add(len(string_zip(s, i)))
        
    return min(result)
    
def string_zip(strs, n):
    result = ""
    target = strs[:n]
    count = 1
    
    for i in range(n, len(strs), n):
        if strs[i:i+n] == target:
            count += 1
        else:
            result += f"{count if count > 1 else ''}{target}"
            count = 1
            target = strs[i:i+n]
        
    result += f"{count if count > 1 else ''}{target}"
    
    return result