# A =[...] B = [...]
# A+B
# 10, 20, 40
# 작은 묶음끼리 먼저 묶고, 클수록 나중에 묶으면 비교가 적어짐.
# 이런 문제의 함정은, 처음에 비교 한 게 무용지물이 됨.
# 왜냐면 카드 묶음이 8개나 된다면?
# 10 50 20 40 60 80 90 100
# 정렬한다고 치자.
# [10,20,40]
# 30[30,40]
# 30+70[70]
# [10,40,20] -> 0 + 10+40 = 50
# [50,20] -> 50 + 70 = 120
# [70]

# [10,20,40,50,60,80,90,100] -> 10+20 = 30
# [30,40,50,60,80,90,100] -> 30 + (30+40) = 100
# [50,60,70,80,90,100] -> 100 + (50+60) = 210
# [70,80,90,100,110] -> 210 + (70+80) = 360
# [90,100,110,150] -> 360 + (90+100) = 550
# [110,150,190] -> 550 + (110+150) = 810
# [190,260] -> 810 + (190+260) = 1260
# 그럼 무슨 말이냐? 최소 힙을 유지하면서, 계속 계산해야 함.
# heapq로 느슨한 정렬 이후.
# while문으로 묶음이 1개 초과일때 동작하도록 한다.
# 그리고 
# 1. (10+20) + (30) + 40 = 100
# 2. (10+40) + (50) + 20 = 120
# n log n

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input().rstrip())
cards = []
count=0

for _ in range(n):
    num = int(input().rstrip())
    heappush(cards, int(num))

while len(cards) >= 2:
    card_a=heappop(cards)
    card_b=heappop(cards)

    heappush(cards, card_a+card_b)
    # print("---",count, card_a, card_b, card_a+card_b, count+card_a+card_b)
    count += card_a+card_b


print(count)