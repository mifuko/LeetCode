class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict

        pos = defaultdict(list)
        
        # 记录每个数出现的位置
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        ans = float('inf')
        
        # 对每个值处理
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # 滑动窗口大小为3
            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i + 2]
                dist = 2 * (right - left)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1