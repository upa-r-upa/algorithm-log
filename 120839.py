win = {"2":"0","0":"5","5":"2"}
def solution(rsp):
    return "".join(list(map(lambda s: win.get(s), list(rsp))))