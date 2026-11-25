# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         L1 = len(word1)
#         L2 = len(word2)
#         merge = ""
#         for i in range(max(L1,L2)):
#             if i < l1:
#                 merge += word1[i]
            
#             if i < l2:
#                 merge += word2[i]

#         return merge

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []

#         for i in range(max(len(word1), len(word2))):
#             if i < len(word1):
#                 result.append(word1[i])
#             if i < len(word2):
#                 result.append(word2[i])

#         return "".join(result)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1

            if j < len(word2):
                result.append(word2[j])
                j += 1

        return "".join(result)