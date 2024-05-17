strings = input()
prev = 0
result = 0

for i, s in enumerate(strings):
	if s == "(":
		prev += 1
	else:
		if strings[i - 1] == "(":
			prev -= 1
			result += prev
		else:
			prev -= 1
			result += 1
		
print(result)