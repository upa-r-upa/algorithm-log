loop = True
while loop:
  a,b=input("").split(" ")
  num_a = int(a)
  num_b = int(b)
  if num_a == 0 and num_b == 0:
    loop = False
  else:
    print("Yes" if num_a > num_b else "No")
