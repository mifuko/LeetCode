### 贪心 每一步都做当前最优的选择，不回头，局部最优=全局最优
# 每个位置能填'a'就填'a'
# 因为'a'是最小的字母，字典序最小
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        word = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if fixed[j] and word[j] != c:
                        return ""
                    word[j], fixed[j] = c, True

        for i, ch in enumerate(str1):
            if ch == "F":
                if any(str2[j - i] != word[j] for j in range(i, i + m)):
                    continue
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        word[j] = "b"
                        break
                else:
                    return ""

        return "".join(word)


### 动态规划 Use dynamic programming. 考虑所有可能，存储结果 局部最优≠全局最优
