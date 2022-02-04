def decode(s):
    hr = int(s[11:13])
    min = int(s[14:16])
    sec = int(s[17:19])
    msec = int(s[20:23])
    dur = float(s[24:-1])
    end = hr * 3600 + min * 60 + sec + msec / 1000
    start = end - dur + 0.001 - 1
    return start, end

def solution(lines):
    timeTable = []
    for line in lines:
        start, end = decode(line)
        print(start)
        print(end)
        print()
        timeTable.append((start, True))
        timeTable.append((end, False))
    timeTable.sort(key=lambda x: x[0])
    answer = 0
    load = 0
    for time in timeTable:
        if time[1]:
            load += 1
            answer = max(answer, load)
        else:
            load -= 1
    return answer