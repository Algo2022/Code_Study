import heapq


class Job():
    def __init__(self, job):
        self.req = job[0]
        self.dur = job[1]

    def __lt__(self, other):
        if self.req < other.req:
            return True
        elif self.req == other.req:
            if self.dur < other.dur:
                return True
        return False

    def __str__(self) -> str:
        return "[{0}, {1}]".format(str(self.req), str(self.dur))


def solution(jobs):
    n = len(jobs)
    wait_time_total = 0
    jobs_heap = [Job(job) for job in jobs]
    heapq.heapify(jobs_heap)
    wait_until = 0
    temp = []
    while True:
        if jobs_heap:
            job_curr = heapq.heappop(jobs_heap)
            if job_curr.req < wait_until:
                temp.append(job_curr)
            else:
                if temp:
                    heapq.heappush(jobs_heap, job_curr)
                    job_next = min(temp, key=lambda x: x.dur)
                    temp.remove(job_next)
                    wait_time_total += wait_until - job_next.req + job_next.dur
                    wait_until += job_next.dur
                    for j in temp:
                        heapq.heappush(jobs_heap, j)
                    temp = []
                    print(job_next)
                else:
                    wait_time_total += job_curr.dur
                    wait_until = job_curr.req + job_curr.dur
                    print(job_curr)
        elif temp:
            job_next = min(temp, key=lambda x: x.dur)
            print(job_next)
            temp.remove(job_next)
            wait_time_total += wait_until - job_next.req + job_next.dur
            wait_until += job_next.dur
            for j in temp:
                heapq.heappush(jobs_heap, j)
            temp = []
        else:
            break
    return wait_time_total // n
