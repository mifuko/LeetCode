func partition(s string) [][]string {
    n := len(s)
    res := [][]string{}

    dp := make([][]bool, n)
    for i := range dp {
        dp[i] = make([]bool, n)
    }

    for i := n - 1; i >= 0; i-- {
        for j := i; j < n; j++ {
            if s[i] == s[j] && (j-i < 3 || dp[i+1][j-1]) {
                dp[i][j] = true
            }
        }
    }

    path := make([]string, 0, n)  // 预分配，避免append过多分配

    var backtrack func(start int)
    backtrack = func(start int) {
        if start == n {
            tmp := make([]string, len(path))
            copy(tmp, path)
            res = append(res, tmp)
            return
        }
        for end := start; end < n; end++ {
            if dp[start][end] {
                // 先截取子串
                sub := s[start : end+1]
                path = append(path, sub)
                backtrack(end + 1)
                path = path[:len(path)-1]
            }
        }
    }

    backtrack(0)
    return res
}
