class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #You must write an algorithm with O(log n) runtime complexity.意味着是对有序数组二分查找，对数级别，不能是线性的O(n)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left  # target 不存在时，left 是插入位置