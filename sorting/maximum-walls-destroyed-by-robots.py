from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        indexed = sorted(zip(robots, distance))
        sorted_walls = sorted(walls)
        n = len(indexed)
        
        # 预处理每个机器人左射和右射能打到的墙的索引范围
        left_ranges = []   # (lo, hi) 在sorted_walls中的下标范围
        right_ranges = []
        
        for i, (pos, dist) in enumerate(indexed):
            # 左射范围
            left_block = indexed[i-1][0] + 1 if i > 0 else 0
            left_start = max(left_block, pos - dist)
            left_lo = bisect_left(sorted_walls, left_start)
            left_hi = bisect_right(sorted_walls, pos)
            left_ranges.append((left_lo, left_hi))
            
            # 右射范围
            right_block = indexed[i+1][0] if i < n-1 else float('inf')
            right_end = min(right_block - 1, pos + dist)
            right_lo = bisect_left(sorted_walls, pos)
            right_hi = bisect_right(sorted_walls, right_end)
            right_ranges.append((right_lo, right_hi))
        
        destroyed = set()
        
        # 关键：考虑相邻机器人之间的墙的归属
        # 对每个gap（相邻两机器人之间），枚举左打右 vs 右打左
        # 但这样会变成全局组合爆炸...
        # 
        # 正确思路：
        # 每个机器人i，左射只打"自己左边gap"的墙
        #             右射只打"自己右边gap"的墙
        # 对于每个gap，由相邻两机器人竞争：
        #   - 左机器人右射 能打到的墙集合 A
        #   - 右机器人左射 能打到的墙集合 B
        #   - 两者并集 = A∪B，但每个机器人只能选一个方向
        # → 对每个gap独立：选A还是选B（取多的那个）
        #   剩下的机器人方向由另一个gap决定
        
        # 重新建模：每个机器人只有左/右两种选择
        # gap i 表示 robots[i] 和 robots[i+1] 之间的墙
        # gap i 的墙只能被 robots[i]右射 或 robots[i+1]左射 覆盖
        # 且 robots[i] 的左射属于 gap i-1，右射属于 gap i
        # → 每个机器人的左射和右射分属两个不同的gap，互相独立！
        # → 所以每个gap独立取max没问题？
        
        # 但等等：robots[i]只有一颗子弹，选了右射就不能左射
        # gap i-1 依赖 robots[i] 左射
        # gap i   依赖 robots[i] 右射
        # 这两个gap共享 robots[i]，所以不独立！
        
        # → 这是一个链式DP问题
        # dp[i] = 前i个机器人最多能打掉多少墙
        # 每个机器人选左或右，影响相邻gap的覆盖
        
        # gap_walls[i] = robots[i]右射 和 robots[i+1]左射 覆盖的墙
        # 具体分：right_of[i] = robots[i]右射打到的墙集合（在gap i中）
        #         left_of[i+1] = robots[i+1]左射打到的墙集合（在gap i中）
        
        # 每个机器人i选左(L)或右(R)：
        # - 选L：贡献 left_of[i] 的墙给 gap i-1
        # - 选R：贡献 right_of[i] 的墙给 gap i
        # gap i 的总墙数 = |right_of[i] ∪ left_of[i+1]|
        #   如果robots[i]选R且robots[i+1]选L → 两者都贡献
        #   如果robots[i]选R但robots[i+1]选R → 只有right_of[i]
        #   如果robots[i]选L且robots[i+1]选L → 只有left_of[i+1]
        #   如果robots[i]选L且robots[i+1]选R → 都不贡献gap i的墙
        
        # DP状态：dp[i][dir] = 前i个机器人，第i个选dir(0=左,1=右)时最多墙数
        
        INF = float('inf')
        
        # 预处理每个gap中，左机右射 和 右机左射 各自能打到哪些墙（用下标集合）
        # gap i: between indexed[i] and indexed[i+1]
        
        def get_walls_set(lo, hi):
            return set(range(lo, hi))
        
        # right_shot[i] = robots[i]右射在gap i（右边gap）中打到的墙下标集合
        # left_shot[i]  = robots[i]左射在gap i-1（左边gap）中打到的墙下标集合
        
        right_shot = []
        left_shot = []
        for i in range(n):
            rlo, rhi = right_ranges[i]
            right_shot.append(set(range(rlo, rhi)))
            llo, lhi = left_ranges[i]
            left_shot.append(set(range(llo, lhi)))
        
        # dp[dir]: 当前机器人选dir时，累计打掉的墙下标集合
        # 但集合DP太慢，改用计数
        
        # 关键观察：gap i的墙只在gap i内，不同gap的墙不重叠
        # 所以总数 = 各gap贡献之和
        # gap i的贡献取决于robots[i]选R还是选L，robots[i+1]选L还是选R
        
        # gap i 的贡献：
        # robots[i]=R, robots[i+1]=L → |right_shot[i] ∪ left_shot[i+1]|
        # robots[i]=R, robots[i+1]=R → |right_shot[i]|
        # robots[i]=L, robots[i+1]=L → |left_shot[i+1]|
        # robots[i]=L, robots[i+1]=R → 0
        
        # DP：dp[i][d] = 前i+1个机器人，第i个选d，最大总墙数
        
        gap_contrib = {}
        for i in range(n-1):
            rs = right_shot[i]
            ls = left_shot[i+1]
            gap_contrib[(i, 'RR')] = len(rs)                    # i选R, i+1选R
            gap_contrib[(i, 'RL')] = len(rs | ls)               # i选R, i+1选L
            gap_contrib[(i, 'LR')] = 0                          # i选L, i+1选R
            gap_contrib[(i, 'LL')] = len(ls)                    # i选L, i+1选L
        
        # 最左机器人左射的墙（gap -1，无左邻居阻挡）
        # 最右机器人右射的墙（gap n，无右邻居阻挡）
        
        # dp[d] = 到当前机器人选d时的最大值
        dp = [0, 0]  # dp[0]=选左, dp[1]=选右
        
        # 初始化第0个机器人
        # 第0个机器人左射：left_shot[0]（左边无其他机器人阻挡，已在left_ranges算好）
        # 第0个机器人右射：先不算，等处理gap 0时再加
        dp[0] = len(left_shot[0])   # 选左，打左边的墙
        dp[1] = 0                    # 选右，左边墙没打
        
        for i in range(1, n):
            new_dp = [0, 0]
            # 当前机器人i选左(0)
            # gap i-1 的贡献：
            #   上一个(i-1)选R → gap_contrib[(i-1,'RL')]
            #   上一个(i-1)选L → gap_contrib[(i-1,'LL')]
            # 当前机器人i自己左射在gap i-1中的贡献已包含在gap_contrib里
            # 但还需加上i左射在"更左"的贡献？不，left_shot[i]就是i左射在gap i-1的墙
            
            new_dp[0] = max(
                dp[1] + gap_contrib[(i-1, 'RL')],  # i-1选R，i选L
                dp[0] + gap_contrib[(i-1, 'LL')]   # i-1选L，i选L
            )
            # 当前机器人i选右(1)
            new_dp[1] = max(
                dp[1] + gap_contrib[(i-1, 'RR')],  # i-1选R，i选R
                dp[0] + gap_contrib[(i-1, 'LR')]   # i-1选L，i选R
            )
            dp = new_dp
        
        # 最后一个机器人如果选右，加上其右射的墙
        dp[1] += len(right_shot[n-1])
        
        return max(dp)