def solution(string):
    stack = []
        
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    
    return 1 if len(stack) == 0 else 0