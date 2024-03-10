s, k, h = map(int, input().split())
schools = {s: "Soongsil", k: "Korea", h: "Hanyang"}

if s + k + h >= 100:
    print('OK')
else:
    print(schools[min(s, k, h)])