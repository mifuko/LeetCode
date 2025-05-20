class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        res = []
        dp = [[False]*n for _ in range(n)]

        # 预处理回文子串
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True

        def backtrack(start: int, path: list[str]):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end+1, path)
                    path.pop()

        backtrack(0, [])
        return res
