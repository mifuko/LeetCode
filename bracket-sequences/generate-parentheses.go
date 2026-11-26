func generateParenthesis(n int) []string {
    var result []string
    var backtrack func(path string, left, right int)
    
    backtrack = func(path string, left, right int) {
        if len(path) == 2*n {
            result = append(result, path)
            return
        }
        
        if left < n {
            backtrack(path+"(", left+1, right)
        }
        
        if right < left {
            backtrack(path+")", left, right+1)
        }
    }
    
    backtrack("", 0, 0)
    return result
}

// 回溯法，使用匿名函数实现递归，通过闭包访问外部的 result 切片。
// 在 Go 语言中，贪心算法通常不适用于生成所有有效括号组合（因为需要穷举所有可能性），但可以用于解决一些特定的括号问题，例如 判断括号字符串是否有效、计算最少添加括号数 等。