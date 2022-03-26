function solution(N: number, number: number) {
    let N_string: string = N.toString()
    let series_of_N: [number, Set<number>][] = [1, 2, 3, 4, 5, 6, 7, 8].map(
        (value: number): [number, Set<number>] => [value, new Set([parseInt(N_string.repeat(value))])]
    )
    let solution_map: Map<number, Set<number>> = new Map(series_of_N)

    for (let ord1 = 1; ord1 < 9; ord1++) {
        if (solution_map.get(ord1)!.has(number)) {
            return ord1
        }
        for (let op1 of solution_map.get(ord1)!) {
            for (let ord2 = 1; ord2 <= Math.min(ord1, 8-ord1); ord2++) {
                for (let op2 of solution_map.get(ord2)!) {
                    solution_map.get(ord1+ord2)!
                        .add(op1+op2)
                        .add(Math.abs(op1-op2))
                        .add(op1*op2)
                    if (op2 != 0 && op1 % op2 == 0) {
                        solution_map.get(ord1+ord2)!.add(op1/op2)
                    }
                    if (op1 != 0 && op2 % op1 == 0) {
                        solution_map.get(ord1+ord2)!.add(op2/op1)
                    }
                }
            }
        }
    }
    return -1
}