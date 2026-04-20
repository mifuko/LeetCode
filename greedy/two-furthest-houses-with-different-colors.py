class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0

        # 从左端出发，从右往左找第一个不同色
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                res = max(res, j)
                break

        # 从右端出发，从左往右找第一个不同色
        for j in range(n):
            if colors[j] != colors[n - 1]:
                res = max(res, n - 1 - j)
                break

        return res