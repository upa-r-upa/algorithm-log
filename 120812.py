def solution(array):
    d=dict()
    r=[]

    for i in range(len(array)):
        v = array[i]

        if v in d: d[v] = d[v] + 1
        else: d[v] = 1

        if len(r) > 0:
            if v in r or d[r[len(r)-1]] < d[v]:
                r=[v]
            elif v not in r and d[r[len(r)-1]] == d[v]: 
                r.append(v)
        else:
            r=[v]

    return -1 if len(r) > 1 else r[len(r)-1]