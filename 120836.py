def solution(n):
    count = 0
    for i in range(1, int(n**(1/2) + 1)):
        if n % i == 0:
            if n // i != i: count += 2
            else: count += 1
    return count