from math import ceil

def solution(progresses, speeds):
    l = len(progresses)
    times = [ceil((100 - progresses[i]) / speeds[i]) for i in range(l)]
    ans = []
    queue = []
    for time in times:
        if not queue:
            queue.append(time)
        else:
            if time > queue[0]:
                ans.append(len(queue))
                queue = [time]
            else:
                queue.append(time)
    ans.append(len(queue))
    return ans

