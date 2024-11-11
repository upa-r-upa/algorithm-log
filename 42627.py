from heapq import heappop, heappush
import math

def solution(jobs):
    jobs = sorted(jobs)
    
    seconds = 0
    excutables = []
    done_jobs = []
    avg = 0
    
    # print("** 최초 정렬 **", jobs)
    
    while jobs or excutables:
        while jobs and jobs[0][0] <= seconds: # 작업이 가능한 것들 찾기
            # print("jobs[0]번 실행 가능함", jobs[0])
            # 이미 있는 작업들도 재정렬됨. log n
            excutable_job = jobs.pop(0)
            heappush(excutables, (excutable_job[1], excutable_job))
        
        if excutables:
            job = heappop(excutables)
            # print("작업 실행함:", job[1], "/현재 초:", seconds)
            done_jobs.append(seconds-job[1][0] + job[1][1])
            
            seconds += job[1][1]
            # print("-> 작업 실행 이후 초:", seconds)
        else:
            # print("실행할 작업 없음", jobs[0], jobs[0][0])
            seconds = jobs[0][0]
            
    
    # print(done_jobs, jobs)
    
    return math.floor(sum(done_jobs) / len(done_jobs))

# 디스크 컨트롤러는 현재 들어온 작업 중
# 동 시간대에 여러개의 작업이 들어올 수 있다.
# 1. 아무것도 없는데 요청이 들어왔다면 -> (가능한) 요청 들어온 것 중에 실행 시간 짧은 순서대로 실행
# 2. 이미 작업 중인데 요청이 들어왔다면 -> (가능한) 요청 들어온 것 중에 실행 시간 짧은 순서대로 실행
# 요점은 어떤 구조를 써야 하는가. 일단 요청 시간별로 정렬은 필요하다.
# jobs가 남아있는 동안 while을 돈다.
# 요청 시간이 현재 시간보다 작은 요청들을 배열에 담는다.
# -> 근데 담을땐 만약 현재가 6초고, 3-4-5초에 요청 온 것들이 있다면 '요청'이 물리적으로 가능하기 때문에
# -> 이젠 '수행 시간' 별로 정렬이 필요하다. 근데, 정렬을 이 과정마다 하면 n log n이 매번 걸린다.
# -> 그러면 heap을 써서 정렬해야 한다. (이게 포인트)
# 근데 이 heap이 그럼 한 타이밍에 전부 실행되어야 하는지? 
# 아니다. 가장 우선순위가 높은 job을 실행하고, 그 다음에 또 현재 남아있는 것들 중에서 우선순위를 재측정 해야한다.
# 그러면 heap은 while 외부에 있어야 함.

# 0 [] [0,9]
# 9 [9] [4,1]
# 10 [9,6] [3,6]
# 16 [9,6,13] [2,7] -> [9,6,13,21]
# -> 23 [9,6,13,21] [1,8] -> [9,6,13,21,30]



