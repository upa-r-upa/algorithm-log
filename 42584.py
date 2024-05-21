def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            idx, d = stack.pop()
            answer[idx] = i - idx
            
        stack.append([i, prices[i]])
        
    for idx, v in stack:
        answer[idx] = len(prices) - idx - 1
         
    return answer