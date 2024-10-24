from functools import cmp_to_key

def compare(a, b):
    if a+b > b+a:
        return -1
    else:
        return 0

def solution(numbers):
    strings = [str(x) for x in numbers]
    sorted_strings = sorted(strings, key=cmp_to_key(compare))
    
    return str(int("".join(sorted_strings)))

# import itertools

# def solution(numbers):
#     result = []
    
#     strings = [str(x) for x in numbers]
#     combi = itertools.permutations(strings)
    
#     for item in combi:
#         result.append("".join(list(item)))
        
#     return str(int(max(result)))