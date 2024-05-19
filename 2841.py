import sys

n, p_max = list(map(int, input().split()))
guitars = [[] for i in range(6)]
count = 0

for i in range(n):
	line, p = list(map(int, sys.stdin.readline().rstrip().split()))
	fingers = guitars[line-1]
	
	if len(fingers) == 0 or fingers[-1] < p:
		count += 1
		fingers.append(p)
	elif fingers[-1] > p:
		while len(fingers) > 0 and fingers[-1] > p:
			fingers.pop()
			count += 1
		
		if len(fingers) == 0 or fingers[-1] != p:
			fingers.append(p)
			count += 1
	
print(count)