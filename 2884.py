h,m = map(int, input().split())
r = h*60+m-45
r_h = r // 60
r_m = r % 60

if r_h < 0: print(24+r_h, r_m)
else:  print(r_h, r_m)