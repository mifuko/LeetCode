class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = 到达(i,j)还剩k次免疫，最大收益
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # 初始化起点
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = coins[0][0]
        dp[0][0][2] = coins[0][0]
        # 如果起点是劫匪，用一次免疫
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # 用一次免疫，变成0
            dp[0][0][2] = 0  # 用一次免疫，变成0
        
        # 填第一行
        for j in range(1, n):
            for k in range(3):
                if dp[0][j-1][k] != -float('inf'):
                    val = coins[0][j]
                    dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k] + val)
                    # 使用免疫
                    if val < 0 and k > 0:
                        dp[0][j][k-1] = max(dp[0][j][k-1], dp[0][j-1][k])
        
        # 填第一列
        for i in range(1, m):
            for k in range(3):
                if dp[i-1][0][k] != -float('inf'):
                    val = coins[i][0]
                    dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k] + val)
                    # 使用免疫
                    if val < 0 and k > 0:
                        dp[i][0][k-1] = max(dp[i][0][k-1], dp[i-1][0][k])
        
        # 填剩余格子
        for i in range(1, m):
            for j in range(1, n):
                val = coins[i][j]
                for k in range(3):
                    # 从上面或左边过来
                    best = max(dp[i-1][j][k], dp[i][j-1][k])
                    if best != -float('inf'):
                        dp[i][j][k] = max(dp[i][j][k], best + val)
                    # 使用免疫
                    if val < 0 and k > 0:
                        best2 = max(dp[i-1][j][k], dp[i][j-1][k])
                        if best2 != -float('inf'):
                            dp[i][j][k-1] = max(dp[i][j][k-1], best2)
        
        return max(dp[m-1][n-1])