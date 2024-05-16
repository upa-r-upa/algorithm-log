strings = input().replace("()", "*")
stack = []
result = 0

for i, s in enumerate(strings):
	if s == "(":
		stack.append(i)
	elif s == ")":
		idx = stack.pop()
		cnt = strings[idx:i].count("*")
		result += cnt + 1
		
print(result)