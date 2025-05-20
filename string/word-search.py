class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        # 有多少个list就是多少行
        cols = len(board[0])
        # 每一行长度相等的时候，随便某一行有多少个元素，就是列

        def backtrack(i, j , word_index):
            #要追踪的就是当前匹配的是哪一个字母——它在 word 里的下标（索引），只传数字，不复制字符串
            #如果直接写word，每次递归都要传一个剩余的字符串，创建新字符串
                if word_index == len(word):
                    return True
                
                if (
                    i < 0 or i >= rows or
                    j < 0 or j >= cols or
                    board[i][j] != word[word_index]
                    ):
                    return False
                
                temp = board[i][j]
                board[i][j] = "#"
                
                res = (
                    backtrack(i+1, j, word_index+1) or
                    backtrack(i-1, j, word_index+1) or
                    backtrack(i, j+1, word_index+1) or
                    backtrack(i, j-1, word_index+1)
                    )

                board[i][j] = temp
                return res

        #遍历所有的格子，i行j列的元素开始
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
                    # 尝试从位置 (i, j) 开始，查找单词 word，从第 0 个字母开始匹配（也就是 word[0]）如果能找到，立即返回 True，否则继续尝试下一个格子。