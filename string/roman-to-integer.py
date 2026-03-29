class Solution:
    def romanToInt(self, s):
        # 罗马数字到整数的映射，考虑减法规则
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            curr_value = roman_map[char]
            # 如果当前值小于等于前一个值，则直接相加；否则，需要减去两倍的前一个值再加当前值
            if curr_value >= prev_value:
                total += curr_value
            else:
                total -= curr_value
            prev_value = curr_value
        
        return total

# 从右向左遍历字符串，通过比较当前字符代表的值和前一个字符的值来自动处理加法和减法