string=input()

i = 0
result = True

while i < len(string):
    s = string[i:]

    if s.startswith("pi") or s.startswith("ka"):
        i += 2
    elif s.startswith("chu"):
        i += 3
    else: 
        result = False
        break
	
print("YES" if result else "NO")