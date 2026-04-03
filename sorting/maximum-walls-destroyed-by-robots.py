from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # 按位置排序机器人
        indexed = sorted(zip(robots, distance))
        sorted_walls = sorted(walls)
        n = len(indexed)
        
        destroyed = set()
        
        for i, (pos, dist) in enumerate(indexed):
            
            # 向左射击范围
            # 左边被相邻机器人阻挡
            left_block = indexed[i-1][0] + 1 if i > 0 else 0
            left_start = max(left_block, pos - dist)
            left_end = pos
            
            # 向右射击范围
            # 右边被相邻机器人阻挡
            right_block = indexed[i+1][0] - 1 if i < n - 1 else float('inf')
            right_end = min(right_block, pos + dist)
            right_start = pos
            
            # 左右哪边能打到更多墙就选哪边
            left_lo = bisect_left(sorted_walls, left_start)
            left_hi = bisect_right(sorted_walls, left_end)
            left_count = left_hi - left_lo
            
            right_lo = bisect_left(sorted_walls, right_start)
            right_hi = bisect_right(sorted_walls, right_end)
            right_count = right_hi - right_lo
            
            # 选墙多的方向，加入结果集
            if left_count >= right_count:
                for j in range(left_lo, left_hi):
                    destroyed.add(sorted_walls[j])
            else:
                for j in range(right_lo, right_hi):
                    destroyed.add(sorted_walls[j])
        
        return len(destroyed)