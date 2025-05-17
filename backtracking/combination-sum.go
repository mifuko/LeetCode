func combinationSum(candidates []int, target int) [][]int {
    sort.Ints(candidates) // 排序以支持剪枝优化
    var result [][]int
    var path []int
    
    var backtrack func(startIdx int, remaining int)
    backtrack = func(startIdx int, remaining int) {
        if remaining == 0 {
            // 找到有效组合
            temp := make([]int, len(path))
            copy(temp, path)
            result = append(result, temp)
            return
        }
        
        for i := startIdx; i < len(candidates); i++ {
            if candidates[i] > remaining {
                break // 剪枝：后续元素更大，无需继续尝试
            }
            // 选择当前元素
            path = append(path, candidates[i])
            // 递归处理剩余目标值，允许重复选当前元素
            backtrack(i, remaining-candidates[i])
            // 回溯：撤销选择
            path = path[:len(path)-1]
        }
    }
    
    backtrack(0, target)
    return result
}