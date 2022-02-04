object Solution {
    def solution(n: Int, times: Vector[Int]): Long = suppl(times, n, 1L, times.max.toLong * n.toLong, 0)

    def suppl(times: Vector[Int], n: Int, left: Long, right: Long, ans: Long): Long = (left > right) match {
        case true => ans
        case _ => {
            val mid = (left + right) / 2
            if (times.foldLeft(0L) { (acc, time) => acc + mid / time.toLong } < n.toLong)
                suppl(times, n, mid+1, right, ans)
            else
                suppl(times, n, left, mid-1, mid)
        }
    }
}