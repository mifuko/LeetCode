### 贪心 每一步都做当前最优的选择，不回头，局部最优=全局最优
# 每个位置能填'a'就填'a'
# 因为'a'是最小的字母，字典序最小
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        word = ['a'] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        
        # 第一步：把T的位置填入str2，标记fixed
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if fixed[i+j] and word[i+j] != str2[j]:
                        return ""  # T和T冲突
                    word[i+j] = str2[j]
                    fixed[i+j] = True
        
        # 第二步：检查F的位置
        for i in range(n):
            if str1[i] == 'F':
                if word[i:i+m] == list(str2):
                    # 完全一样，必须改一个字符
                    changed = False
                    for j in range(m):
                        if not fixed[i+j]:  # 找没被T占用的位置
                            word[i+j] = 'b' if str2[j] == 'a' else 'a'
                            changed = True
                            break
                    if not changed:
                        return ""  # 没有可以改的位置
        
        return "".join(word)
            



### 动态规划 Use dynamic programming. 考虑所有可能，存储结果 局部最优≠全局最优
