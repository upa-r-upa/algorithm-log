def solution(price):
    def c(d):
        return int(price * d)

    if price >= 500000:
        return c(.80)
    elif price >= 300000:
        return c(.90)
    elif price >= 100000:
        return c(.95)
    else:
        return price
