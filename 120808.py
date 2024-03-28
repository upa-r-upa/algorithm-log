def solution(n1, d1, n2, d2):
    n=n1*d2 + n2*d1
    d=d1*d2
    
    for i in range(min(n,d)+1,0,-1):
        if n%i==0 and d%i==0:
            n = n // i
            d = d // i
            
    return [n,d]
