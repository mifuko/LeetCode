class Solution:
    # 用于创建类，封装数据和方法，实现面向对象编程。

    def letterCombinations(self, digits: str) -> List[str]:
        # 用于创建独立的函数或类的方法，实现代码复用。

        if not digits:
            return []
        # 先检查是否为空，直接返回 []

        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combination = [""]

        for d in digits:
            letters = digit_map[d]
            new_combination = []
            for prefix in combination:
                for letter in letters:
                    new_combination.append(prefix + letter)
            combination = new_combination
        return combination
