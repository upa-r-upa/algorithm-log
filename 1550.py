a=list(input(""))
dic={"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
result=0
for idx in range(len(a)):
  m=a[len(a) -1 - idx]
  n=int(m) if m not in dic else dic[m] 
  result+=16**idx*n
print(result)
