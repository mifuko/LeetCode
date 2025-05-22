class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 左半边有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左边
                else:
                    left = mid + 1   # 在右边
            # 右半边有序
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右边
                else:
                    right = mid - 1  # 在左边

        return -1