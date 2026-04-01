class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')  # 初始设为无限大
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # 更新最低价格
            else:
                max_profit = max(max_profit, price - min_price)   # 计算今天卖出的利润，更新最大利润
        
        return max_profit