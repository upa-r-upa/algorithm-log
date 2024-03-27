def solution(my_string, overwrite_string, s):
    e = s+len(overwrite_string)
    t = my_string[s:e]
    
    return my_string[:s] + overwrite_string + my_string[e:]