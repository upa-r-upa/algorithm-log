import sys

n, p_max = list(map(int, input().split(" ")))
guitars = [[] for i in range(6)]
count = 0

for i in range(n):
	line, p = list(map(int, sys.stdin.readline().rstrip().split(" ")))
	fingers = guitars[line-1]
	
	if len(fingers) == 0 or fingers[len(fingers)-1] < p:
		count += 1
		fingers.append(p)
	elif fingers[len(fingers)-1] > p:
			if fingers[0] == p:
				count += len(fingers) - 1
				fingers = [p]
			elif fingers[0] > p:
				count += len(fingers) + 1
				fingers = [p]

			else:
				for j in range(len(fingers)):
					if fingers[j] > p:
						count += len(fingers) - j + 1
						fingers = fingers[:j]
						fingers.append(p)
						
						break
					elif fingers[j] == p:
						count += len(fingers) - j - 1
						fingers = fingers[:j+1]
						
						break
	
	guitars[line-1] = fingers
	
print(count)