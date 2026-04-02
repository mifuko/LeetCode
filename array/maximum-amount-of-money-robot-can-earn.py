class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = -float('inf')
        
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        
        # 起点初始化
        dp[0][0][2] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # 用一次免疫
        else:
            dp[0][0][1] = coins[0][0]
        dp[0][0][0] = coins[0][0]  # 不管正负，不用免疫（起点负数也忍着）
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = coins[i][j]
                for k in range(3):
                    # 从上或左过来
                    prev = NEG_INF
                    if i > 0 and dp[i-1][j][k] != NEG_INF:
                        prev = max(prev, dp[i-1][j][k])
                    if j > 0 and dp[i][j-1][k] != NEG_INF:
                        prev = max(prev, dp[i][j-1][k])
                    if prev != NEG_INF:
                        dp[i][j][k] = max(dp[i][j][k], prev + val)
                    # 使用一次免疫（从k+1层过来）
                    if val < 0 and k < 2:
                        prev2 = NEG_INF
                        if i > 0 and dp[i-1][j][k+1] != NEG_INF:
                            prev2 = max(prev2, dp[i-1][j][k+1])
                        if j > 0 and dp[i][j-1][k+1] != NEG_INF:
                            prev2 = max(prev2, dp[i][j-1][k+1])
                        if prev2 != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], prev2)
        
        return max(dp[m-1][n-1])