h,m = map(int, input().split())
need_m = int(input())

r = h*60+m+need_m
r_h = r // 60
r_m = r % 60

if r_h >= 24: print(r_h-24, r_m)
else:  print(r_h, r_m)