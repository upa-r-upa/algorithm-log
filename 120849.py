exclude_str = ["a", "e", "i", "o", "u"]

def solution(my_string):
    result = my_string
    for i in exclude_str:
        result = result.replace(i, "")
        
    return result