# 满足时间复杂度O(n) 空间复杂度O(1)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = 0
#         for n in nums:
#             result ^= n
#         return result


# ### 对每个数，去整个数组里找有没有一样的数。找到了说明它出现了两次，忽略它。找不到说明它只出现一次，返回它。
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             found_pair = False
#             for j in range(len(nums)):
#                 if i != j and nums[i] == nums[j]: #如果不是同一个位置，但值相同
#                     found_pair = True
#                     break
#             if not found_pair:
#                 return nums[i]

### 如果不止出现两次，可能有多次的情况，异或就不管用了，用 HashMap 来统计次数
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}    #count 就是一个字典（dict），用来记录每个数字出现的次数。
        for n in nums:
            count[n] = count.get(n, 0) + 1
            #取 n 的值，如果不存在就默认为 0。
            # `count.get(n, 0)`去字典里查 n 出现过几次，如果没有记录就返回0。 
            #`... + 1`在原来的次数上加1。 `count[n] = ...` 把新的次数存回去。
            
        for n, c in count.items(): 
            # 写法1：拆包，直接给名字
            # 遍历字典里每一对键值，`n` 是数字，`c` 是次数。 
            # count.items() 就是把字典里每一对键值，变成一个个小元组。
            # n, c 就是把元组的第一个给n，第二个给c。
                if c == 1:
                    return n

# 写法2：不拆包，用下标访问 
# count.items() 是字典自带的一个方法，作用是把字典里所有的键值对都取出来。
# 把字典变成了一个装着元组的列表
# for item in count.items():
#     if item[1] == 1:      # item[1] 就是次数
#         return item[0]    # item[0] 就是数字


#count = {2: 3, 3: 1}
#         ↑  ↑
#        键  值
#        数字 次数
# count[2]   # → 3，数字2出现了3次
# count[3]   # → 1，数字3出现了1次
# count = {2: 3, 3: 1}

# count.items() = [(2, 3), (3, 1)]
#                   ↑  ↑    ↑  ↑
#                 数字 次数 数字 次数