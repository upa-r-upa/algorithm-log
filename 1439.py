s = input()
s_1 = " ".join(s.split("0")).split()
s_0 = " ".join(s.split("1")).split()

print(min(len(s_1), len(s_0)))