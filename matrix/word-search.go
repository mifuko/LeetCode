func exist(board [][]byte, word string) bool {
    rows := len(board)
    cols := len(board[0])

    var backtrack func(i, j, wordIndex int) bool
    backtrack = func(i, j, wordIndex int) bool {
        if wordIndex == len(word) {
            return true
        }

        if i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != word[wordIndex] {
            return false
        }

        // 标记当前格子为访问过，防止重复使用
        temp := board[i][j]
        board[i][j] = '#'

        res := backtrack(i+1, j, wordIndex+1) ||
            backtrack(i-1, j, wordIndex+1) ||
            backtrack(i, j+1, wordIndex+1) ||
            backtrack(i, j-1, wordIndex+1)

        // 恢复当前格子状态，回溯
        board[i][j] = temp
        return res
    }

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if backtrack(i, j, 0) {
                return true
            }
        }
    }

    return false
}
