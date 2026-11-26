class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # 遇到开括号，压入栈
                stack.append(char)
            elif char in mapping.keys():  # 遇到闭括号
                if not stack or stack.pop() != mapping[char]:  # 检查是否匹配，不匹配则立即返回False
                    return False
            else:  # 遇到非括号字符，视为无效
                return False
        
        return not stack  # 若栈为空，说明所有括号都已正确匹配

# 早停优化