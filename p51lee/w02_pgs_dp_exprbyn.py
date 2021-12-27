def solution(N, number):
    N_string = str(N)
    series_of_N = [int(N_string * i) for i in range(1, 9)]
    solution_dict = {i: {series_of_N[i - 1]} for i in range(1, 9)}

    for sol in range(1, 9):
        if number in solution_dict[sol]:
            return sol

        for num in solution_dict[sol]:

            for order, srs in enumerate(series_of_N[:8 - sol]):
                solution_dict[sol + 1 + order].add(num + srs)
                solution_dict[sol + 1 + order].add(abs(num - srs))
                solution_dict[sol + 1 + order].add(num * srs)
                if num % srs == 0:
                    solution_dict[sol + 1 + order].add(num / srs)
                if num != 0 and srs % num == 0:
                    solution_dict[sol + 1 + order].add(srs / num)

            for prev_sol in range(1, min(sol, 8 - sol) + 1):
                for eqn_num in solution_dict[prev_sol]:
                    solution_dict[sol + prev_sol].add(num + eqn_num)
                    solution_dict[sol + prev_sol].add(abs(num - eqn_num))
                    solution_dict[sol + prev_sol].add(num * eqn_num)
                    if eqn_num != 0 and num % eqn_num == 0:
                        solution_dict[sol + prev_sol].add(num / eqn_num)
                    if num != 0 and eqn_num % num == 0:
                        solution_dict[sol + prev_sol].add(eqn_num / num)

    return -1