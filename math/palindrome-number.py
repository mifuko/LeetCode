class Solution:
    def isPalindrome(self, x):
        if x < 0:  # 负数不是回文数
            return False
        
        original_x = x
        reversed_x = 0
        
        while x > 0:
            # 提取最低位数字并添加到反转数的末尾
            reversed_x = (reversed_x * 10) + (x % 10)
            # 移除x的最低位
            x //= 10
        
        # 比较原数和反转后的数是否相等
        return original_x == reversed_x
    
# 找到原数字的翻转数，比较原数和反转后的数是否相等