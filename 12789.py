def solution(n, origin):
	arr = []
	idx = 0
	
	for item in origin:
		if item == idx + 1:
			idx += 1
		else:
			arr.append(item)
	
		for _ in range(len(arr)):
			if arr[len(arr) - 1] == idx + 1:
				idx += 1
				arr.pop()
			else:
				break
                
	for _ in range(len(arr)):
		if arr[len(arr) - 1] != idx + 1:
			return print("Sad")
		else:
			idx += 1
			arr.pop()
			
	return print("Nice")
	
solution(int(input()), list(map(int, input().split(" "))))