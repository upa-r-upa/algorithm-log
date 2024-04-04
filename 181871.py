def solution(myString, pat):
    result = 0
    
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            result += 1
        
    return result