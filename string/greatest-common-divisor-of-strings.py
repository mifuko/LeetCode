# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         shorter = str1 if len(str1) < len(str2) else str2

#         for i in range(len(shorter), 0, -1):
#             division = shorter[:i]

#             if (str1 == division * (len(str1) // i)
#                 and str2 == division * (len(str2) // i)):
#                 return division

#         return ""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]