test_case=int(input(""))

for idx in range(test_case):
  num = int(input(""))
  crease_num = 1;
  save_set=[]
  
  while True:
    if crease_num >= num / 2:
      print(f"Pairs for {num}:{','.join(save_set)}")
      
      break
    
    minus = num - crease_num

    if crease_num + minus == num:
      save_set.append(f" {crease_num} {minus}")
      
    crease_num += 1
