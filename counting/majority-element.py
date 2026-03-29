### 时间O(n) 空间O(n)
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

# count 代表当前候选人还剩多少人没被抵消
# 一旦被抵消完（count=0），说明之前的候选人出局，换新的
# 因为多数派人数超过一半，最后一定是多数派活到最后