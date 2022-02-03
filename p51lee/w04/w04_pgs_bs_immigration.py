def greedy_solution(n, times):
    times_tot = times[:]
    for _ in range(n):
        min_index = times_tot.index(min(times_tot))
        times_tot[min_index] += times[min_index]
    for i, time in enumerate(times):
        times_tot[i] -= time
    return max(times_tot)
