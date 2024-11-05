def solution(string):
    count = 0
    
    for i in range(len(string)):
        stack = []
        rotate_str = string[i:] + string[:i]
        
        for s in rotate_str:
            if s == "(" or s == "{" or s == "[":
                stack.append(s)
            elif stack and ((s == ")" and stack[-1] == "(") or (s == "}" and stack[-1] == "{") or (s == "]" and stack[-1] == "[")):
                stack.pop()
            else:
                break
        else:
            if len(stack) == 0:
                count += 1
    
    return count
