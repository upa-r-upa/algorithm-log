def solution(emergency):
    result = sorted(emergency, reverse=True)
    return [result.index(v) + 1 for v in emergency]