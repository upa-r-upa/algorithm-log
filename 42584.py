def solution(prices):
    result = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            result[j] = i-j
        
        stack.append(i)
        
        
    for k in stack:
        result[k] = len(prices) - (k + 1)
    
    return result
