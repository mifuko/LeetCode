class Solution:
    def twoSum(self, nums, target):
        # 初始化一个空列表用于存储找到的索引对
        solution = []

        # 使用两层循环遍历所有可能的数对
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # j 从 i+1 开始避免重复检查和自加
                if nums[i] + nums[j] == target:  # 当找到和为目标值的数对时
                    # 将这对索引添加到 solution 列表中
                    solution.append([i, j])
                    # 注意：题目假设只有一个解，但这段代码会找到所有解。若只需要一个解，可在此处直接返回 solution 并终止循环。

        # 理论上题目保证有解，但此处仍应有返回值处理逻辑以应对无解情况（尽管题目假设这种情况不存在）
        if solution:  # 如果找到了解
            return solution[0]  # 返回第一个找到的解，根据题目要求
        else:
            return []  # 或者抛出异常，因为题目假设必定有解

# 示例调用
solution_instance = Solution()
print(solution_instance.twoSum([2, 7, 11, 15], 9))  # 应输出 [0, 1]

#暴力枚举