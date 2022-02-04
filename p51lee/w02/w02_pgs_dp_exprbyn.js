var __values = (this && this.__values) || function(o) {
    var s = typeof Symbol === "function" && Symbol.iterator, m = s && o[s], i = 0;
    if (m) return m.call(o);
    if (o && typeof o.length === "number") return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
    throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
};
function solution(N, number) {
    var e_1, _a, e_2, _b;
    var N_string = N.toString();
    var series_of_N = [1, 2, 3, 4, 5, 6, 7, 8].map(function (value) { return [value, new Set([parseInt(N_string.repeat(value))])]; });
    var solution_map = new Map(series_of_N);
    for (var ord1 = 1; ord1 < 9; ord1++) {
        if (solution_map.get(ord1).has(number)) {
            return ord1;
        }
        try {
            for (var _c = (e_1 = void 0, __values(solution_map.get(ord1))), _d = _c.next(); !_d.done; _d = _c.next()) {
                var op1 = _d.value;
                for (var ord2 = 1; ord2 <= Math.min(ord1, 8 - ord1); ord2++) {
                    try {
                        for (var _e = (e_2 = void 0, __values(solution_map.get(ord2))), _f = _e.next(); !_f.done; _f = _e.next()) {
                            var op2 = _f.value;
                            solution_map.get(ord1 + ord2)
                                .add(op1 + op2)
                                .add(Math.abs(op1 - op2))
                                .add(op1 * op2);
                            if (op2 != 0 && op1 % op2 == 0) {
                                solution_map.get(ord1 + ord2).add(op1 / op2);
                            }
                            if (op1 != 0 && op2 % op1 == 0) {
                                solution_map.get(ord1 + ord2).add(op2 / op1);
                            }
                        }
                    }
                    catch (e_2_1) { e_2 = { error: e_2_1 }; }
                    finally {
                        try {
                            if (_f && !_f.done && (_b = _e["return"])) _b.call(_e);
                        }
                        finally { if (e_2) throw e_2.error; }
                    }
                }
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c["return"])) _a.call(_c);
            }
            finally { if (e_1) throw e_1.error; }
        }
    }
    return -1;
}
