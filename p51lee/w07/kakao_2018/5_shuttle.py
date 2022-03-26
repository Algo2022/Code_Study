from collections import deque

def absTime(time):
    h, m = map(int, time.split(":"))
    return 60 * h + m

def stringify(absTime):
    h = absTime // 60
    m = absTime % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2)

def solution(n, t, m, timetable):
    absTimeTable = deque(sorted(map(absTime, timetable)))
    seatMat= [[] for _ in range(n)]
    shuttleTime = 60 * 9
    shuttleIndex = 0
    while absTimeTable and shuttleIndex < n:
        crewTime = absTimeTable.popleft()
        if crewTime <= shuttleTime and len(seatMat[shuttleIndex]) < m:
            seatMat[shuttleIndex].append(crewTime)
        else:
            shuttleTime += t
            absTimeTable.appendleft(crewTime)
            shuttleIndex += 1
    print(seatMat)
    trivialSol= seatMat[-1][-1]-1 if seatMat[-1] else 0
    for i, crews in reversed(list(enumerate(seatMat))):
        if len(crews) < m:
            return stringify(max(60 * 9 + i * t, trivialSol))
    return stringify(trivialSol)
