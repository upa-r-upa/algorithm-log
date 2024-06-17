s = list(input())

is_tag = False
word = []

for i in range(len(s)):
	if s[i] == ">":
		is_tag = False
	elif is_tag is False and (s[i] == " " or s[i] == "<"):
		s[i-len(word):i] = word[::-1]
		word=[]
		if s[i] == "<":
			is_tag = True
	elif is_tag is False:
		word.append(s[i])
		if i + 1 == len(s):
			s[i+1-len(word):] = word[::-1]
	
print(*s, sep="")