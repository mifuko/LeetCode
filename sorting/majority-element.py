### 时间O(n) 空间O(n) 词典
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}

#         for n in nums:
#             count[n] = count.get(n, 0) + 1 

#         for n, c in count.items():
#             if c > len(nums) / 2:
#                 return n

# Step 1: Create an empty dictionary
# Step 2: Count the occurrences of each number
# We loop through every number in the array. For each number, we check how many times it has appeared so far using `count.get(n, 0)` — if it hasn't appeared before, we start from 0. Then we add 1 to record this new occurrence and store it back in the dictionary.
# Step 3: Find the majority element
# We loop through the dictionary. For each number `n` with count `c`, we check if it appears more than half the length of the array. If yes, that's our answer and we return it.

# count.get(n, 0)look up one keywhen adding to count
# count.items()take out all pairswhen searching for answer


### Boyer-Moore投票算法
### 时间O(n) 空间O(1) 只用了两个变量 没有任何字典或者列表
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for n in nums:
            if count == 0:
                candidate = n   # 重新选候选人
            if n == candidate:
                count += 1      # 同阵营，+1
            else:
                count -= 1      # 不同阵营，抵消
        
        return candidate

# candidate = 当前"活着"的那个数字
# count = 它比其他数字多出来几个，还没被抵消的，不是出现次数，而是领先优势
# 因为多数派人数超过一半，最后一定是多数派活到最后

# The cancellation rule:
# Same as candidate → they're on the same team, count + 1
# Different from candidate → they cancel each other out, count - 1
# Count hits 0 → the current candidate has been fully cancelled, pick a new one

# Why the majority element always wins:
# Because the majority element appears more than n/2 times, even if every single minority element cancels it out one by one, there will still be majority elements left standing at the end. The minority simply doesn't have enough people to fully cancel the majority.