n=int(input())
r = ""
if n >= 90:
    r = "A"
elif n >= 80:
    r = "B"
elif n >= 70:
    r = "C"
elif n >= 60:
    r = "D"
else:
    r = "F"

print(r)