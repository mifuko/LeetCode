class Solution_BT:
    # 回溯法（Backtracking）

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(n, "", 0, 0, result)
        # self.backtrack：表示调用当前类的实例方法backtrack 因为 backtrack 是类中的方法，需要通过 self 访问类的属性或其他方法。是整个回溯过程的起点
        # backtrack 是一个递归函数，用于在递归过程中尝试所有可能的选择，并在满足条件时记录结果或回溯（撤销选择）。
        return result
    
    def backtrack(self, n: int, path: str, left: int, right: int, result: List[str]):
        # 终止条件：括号序列长度为 2n
        if len(path) == 2 * n:
            result.append(path)
            return
        
        # 选择1：添加左括号（如果左括号数量未用完）
        if left < n:
            self.backtrack(n, path + "(", left + 1, right, result)
        
        # 选择2：添加右括号（如果右括号数量少于左括号）
        if right < left:
            self.backtrack(n, path + ")", left, right + 1, result)


# def backtrack(self, n: int, path: str, left: int, right: int, result: List[str]):
# 参数	    含义
# n	        目标括号对数（例如 n=3 表示生成 3 对括号）。
# path	    当前正在构建的括号字符串（例如 "((" 或 "(())"）。初始为空字符串 ""
# left	    已使用的左括号数量（初始为 0，最大为 n）。
# right	    已使用的右括号数量（初始为 0，最大为 left）。
# result	用于存储所有有效括号字符串的列表（全局结果）。初始为 []（在 generateParenthesis 函数中创建）

# 时间复杂度：卡特兰数（Catalan number）的复杂度，因为每个有效序列的长度为 
# 空间复杂度：O(n)，递归栈的最大深度为 2n

class Solution_BFS:
     # BFS（Backtracking）
     # 通过队列逐层生成所有可能的括号组合，每一步添加左括号或右括号，并检查其有效性。

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque([("", 0, 0)])  
        # 初始化队列，每个元素是一个元组 (当前字符串, 左括号数, 右括号数)，初始状态为 ("", 0, 0)（空字符串，0 个左括号，0 个右括号）。
        # deque：用于实现队列（双端队列），提供高效的 popleft() 操作（时间复杂度 (O(1))）

        while queue:
            s, left, right = queue.popleft()
            # 从队列头部取出元素，赋值给 s（当前字符串）、left（已用左括号数）、right（已用右括号数）。
            # 终止条件：生成的字符串长度达到 2n

            if len(s) == 2 * n:
                result.append(s)
                continue
            # 将 s 添加到 result 中，并通过 continue 跳过本次循环的后续操作（不再添加括号）。

            # 若已用左括号数 left 小于 n，说明还可以添加左括号 
            if left < n:
                queue.append((s + "(", left + 1, right))
            
            # 若已用右括号数 right 小于左括号数 left，说明可以添加右括号 )（确保右括号不超过左括号，避免无效序列）。
            if right < left:
                queue.append((s + ")", left, right + 1))
        
        return result


class Solution:
     # 贪心构造法
     # 核心观察：每个有效括号组合的前缀中，左括号数量必须 始终不少于 右括号数量。
     # 贪心策略：优先添加左括号，直到无法添加（数量达到 n）。必须添加右括号时，确保剩余右括号数量足够补全（即 剩余右括号数 = n - 当前右括号数 > 0）。

    def generateParenthesis(self, n: int) -> List[str]:  # 添加self参数
        result = []
        
        def backtrack(path: str, left: int, right: int):  
            # backtrack 是 generateParenthesis 内部的辅助函数，属于generateParenthesis方法
            # 当前已生成的括号字符串（如 "(()"）
            if len(path) == 2 * n:
                result.append(path)
                return
            # 当 path 的长度达到 2n 时（例如 n=3 时长度为 6），说明已生成完整的括号组合。
            # 将 path 添加到 result 中，并通过 return 回溯到上一层递归。

            if left < n:
                backtrack(path + "(", left + 1, right)
            # right 不变：右括号数量未增加。

            if right < left:
                backtrack(path + ")", left, right + 1)
        
        backtrack("", 0, 0)  
        # 调用backtrack函数启动递归,初始状态
        return result # return result 属于 generateParenthesis 方法