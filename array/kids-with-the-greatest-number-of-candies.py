# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         res = []

#         for i in range(len(candies)):
#             if candies[i] + extraCandies >= max(candies):
#                 res.append(True)
#             else:
#                 res.append(False)

#         return res


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]