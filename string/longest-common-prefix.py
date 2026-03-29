class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # 初始化最长公共前缀为第一个字符串
        prefix = strs[0]

        # 遍历字符串列表中的每个字符串，从第二个字符串开始
        for s in strs[1:]:
            # 如果当前前缀为空，直接返回空字符串
            if not prefix:
                return prefix
            # 检查当前字符串是否包含当前的最长公共前缀
            while not s.startswith(prefix):
                # 如果不包含，缩短前缀
                prefix = prefix[:-1]
                # 如果前缀为空，说明不存在公共前缀
                if not prefix:
                    return ""

        return prefix

