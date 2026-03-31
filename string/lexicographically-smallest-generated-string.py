### 贪心 每一步都做当前最优的选择，不回头，局部最优=全局最优
# 每个位置能填'a'就填'a'
# 因为'a'是最小的字母，字典序最小
# class Solution:
#     def generateString(self, str1: str, str2: str) -> str:
#         n, m = len(str1), len(str2)
#         word = ["a"] * (n + m - 1)
#         fixed = [False] * (n + m - 1)

#         for i, ch in enumerate(str1):
#             if ch == "T":
#                 for j, c in enumerate(str2, i):
#                     if fixed[j] and word[j] != c:
#                         return ""
#                     word[j], fixed[j] = c, True

#         for i, ch in enumerate(str1):
#             if ch == "F":
#                 if any(str2[j - i] != word[j] for j in range(i, i + m)):
#                     continue
#                 for j in range(i + m - 1, i - 1, -1):
#                     if not fixed[j]:
#                         word[j] = "b"
#                         break
#                 else:
#                     return ""

#         return "".join(word)


### 动态规划 Use dynamic programming. 考虑所有可能，存储结果 局部最优≠全局最优



### 社区方法 函数Z
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1)
        
        # 计算Z函数
        def calc_z(s):
            n = len(s)
            z = [0] * n
            z[0] = n
            box_l = box_r = 0
            for i in range(1, n):
                if i <= box_r:
                    z[i] = min(z[i - box_l], box_r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    box_l, box_r = i, i + z[i]
                    z[i] += 1
            return z
        
        # 第一步：处理T
        z = calc_z(str2)
        pre = -m
        for i, ch in enumerate(str1):
            if ch != 'T':
                continue
            size = max(pre + m - i, 0)
            # 重叠部分前缀和后缀必须一致
            if size > 0 and z[m - size] < size:
                return ""
            # 填入str2中size之后的部分
            for j in range(size, m):
                ans[i + j] = str2[j]
            pre = i
        
        # 记录'?'的位置，填成'a'
        pre_q = [-1] * len(ans)
        pre = -1
        for i in range(len(ans)):
            if ans[i] == '?':
                ans[i] = 'a'
                pre = i
            pre_q[i] = pre
        
        # 用Z函数找ans中和str2匹配的位置
        z = calc_z(str2 + "".join(ans))
        
        # 第二步：处理F
        i = 0
        while i < n:
            if str1[i] == 'F':
                # z[m+i]>=m 说明ans从i开始和str2完全匹配
                if z[m + i] >= m:
                    j = pre_q[i + m - 1]
                    if j < i:
                        return ""
                    ans[j] = 'b'
                    i = j  # 直接跳到j，后面包含'b'的子串一定不等于str2
            i += 1
        
        return "".join(ans)