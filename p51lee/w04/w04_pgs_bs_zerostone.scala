object Solution {
    def solution(distance: Int, rocks: Vector[Int], n: Int): Int = suppl((rocks :+ distance).sorted, n, 1, distance, 0)

    def suppl(rocks: Vector[Int], n: Int, left: Int, right: Int, ans: Int): Int = (left > right) match {
        case true => ans
        case _ => {
            val mid = (left + right) / 2
            rocks.foldLeft((0, 0)) { (acc, rock) =>
                acc match { case (current, remove) => {
                    if (rock-current < mid) (current, remove+1) else (rock, remove)
                }}
            } match { case (current, remove) => {
                if (remove > n) suppl(rocks, n, left, mid-1, ans) else suppl(rocks, n, mid+1, right, mid)
            }}
        }
    }
}