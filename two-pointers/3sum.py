class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)
        
        if n < 3:
            return []
        
        # 特殊情况处理：数组中只包含0的情况
        if set(nums) == {0} and n >= 3:
            return [[0, 0, 0]]
        
        for i in range(n - 2):
            # 跳过重复的元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] > 0:  # 数组已经排序，如果当前元素大于0，则后续元素也大于0，不可能使和为0
                break
            
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    # 对于当前nums[i]，找到一组解，先添加
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的nums[left]和nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 移动指针
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        # 去重
        unique_results = []
        for triplet in result:
            if triplet not in unique_results:
                unique_results.append(triplet)
        
        return unique_results