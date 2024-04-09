import re

s = input()
k = input()

string = re.sub(r'\d', "", s)

print(int(k in string))