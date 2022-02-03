object Solution {
    def solution(numbers: Vector[Int]): String = {
        val ans = numbers
            .map(_.toString)
            .sortWith((s, t) => s.concat(t).toInt > t.concat(s).toInt)
            .mkString("")
        if (ans.startsWith("0")) "0" else ans
    }
}