a,b,c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a != b and b != c and a != c:
    print(max(a,b,c)*100)
else:
    eye = a if a == b or a == c else b
    print(1000+eye*100)