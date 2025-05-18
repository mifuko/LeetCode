class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  
        # 存储所有排列结果
        used = [False] * len(nums)  
        # 标记数组，记录哪些数字已经被使用过

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())  
                # 注意要复制一份当前的路径，避免后续修改影响结果
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])  # 选择当前数字
                    used[i] = True       # 标记为已使用

                    backtrack(path)      # 递归进入下一层

                    path.pop()           # 撤销选择（回溯）
                    used[i] = False      # 恢复为未使用

        backtrack([])  # 从空路径开始回溯
        return res

class Solution:
    def permute(self, nums):
        res = []
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # 复制当前排列并加入结果
                return
            for i in range(len(nums)):
                if not used[i]:
                    # 做选择
                    path.append(nums[i])
                    used[i] = True

                    # 递归
                    backtrack(path, used)

                    # 回溯 把状态恢复到递归之前的样子，保证下次尝试不同选择时不受影响。
                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        # path 初始是 []（空列表）
        # used 初始是 [False, False, ..., False]（长度和 nums 一样，表示都没用过）
        # 递归里每次调用 backtrack(path, used) 都是传着当前的 path 和 used 状态继续往下走。
        # 所以 path 和 used 的定义和初始化都集中在递归入口处。
        return res

