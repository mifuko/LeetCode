class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top, bot = x, x + k - 1
        while top < bot:
            for col in range(y, y + k):
                grid[top][col], grid[bot][col] = grid[bot][col], grid[top][col]
            top += 1
            bot -= 1
        return grid