### 总共4个 直接对应 用sort来列表和列表比较
# class Solution:
#     def canBeEqual(self, s1: str, s2: str) -> bool:
#         return sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])


### 拆分 用变量把每组字符存起来

# class Solution:
#     def canBeEqual(self, s1: str, s2: str) -> bool:
#         s1_odd = sorted([s1[0], s1[2]])   # s1的0,2位置
#         s1_even = sorted([s1[1], s1[3]])  # s1的1,3位置
#         s2_odd = sorted([s2[0], s2[2]])   # s2的0,2位置
#         s2_even = sorted([s2[1], s2[3]])  # s2的1,3位置
        
#         return s1_odd == s2_odd and s1_even == s2_even


# sorted() 可以对任何可迭代的东西用 不管输入是什么，返回的永远是列表
# 列表
# sorted([3, 1, 2])          # → [1, 2, 3]
# 字符串
# sorted("bac")              # → ['a', 'b', 'c']
# 元组
# sorted((3, 1, 2))          # → [1, 2, 3]
# 字典（默认对键排序）
# sorted({2: 'b', 1: 'a'})   # → [1, 2]

# sorted(nums)    # ✅ 不改变原来的，返回新列表
# nums.sort()     # ✅ 直接改变原来的列表，不返回新的

### 切片法 直接用字符串切片
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])