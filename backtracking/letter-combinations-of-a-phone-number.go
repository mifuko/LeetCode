func letterCombinations(digits string) []string {
    
    //参数：digits string，输入的数字字符串（类型为 string）。
    //返回值：[]string，表示返回一个字符串切片（动态数组）。

    if len(digits) == 0 {
        return []string{}
    }

    //等价于 return make([]string, 0)   使用 make 函数创建空切片
    //获取字符串长度。若输入为空字符串（""），直接返回空切片。
    //[]string：创建一个字符串类型的切片（slice）。{}：初始化一个空的切片值。
    
    digitMap := map[byte][]string{
        '2': {"a", "b", "c"},
        '3': {"d", "e", "f"},
        '4': {"g", "h", "i"},
        '5': {"j", "k", "l"},
        '6': {"m", "n", "o"},
        '7': {"p", "q", "r", "s"},
        '8': {"t", "u", "v"},
        '9': {"w", "x", "y", "z"},
    }

    //定义一个字典（映射），键为 byte 类型（ASCII 码），值为字符串切片。
    //在 Go 中，字符串的字符本质是 byte（UTF-8 编码），因此 digits[i] 返回的是 byte 类型（如 '2' 的 ASCII 码为 50）。

    combinations := []string{""}
    
    //初始化为包含一个空字符串 "" 的切片。

    for i := 0; i < len(digits); i++ {
        d := digits[i]
        letters, exists := digitMap[d]
        if !exists {
            continue
        }

        //digits[i]：获取第 i 个字符的 byte 值（如 "23" 中第一个字符 '2'）。
        //exists 是一个布尔值，表示键是否存在。

        newCombinations := []string{}
        for _, prefix := range combinations {
            for _, letter := range letters {
                newCombinations = append(newCombinations, prefix+letter)
            }
        }
        combinations = newCombinations
    }
    
    //外层循环遍历当前所有组合（prefix）。
    //内层循环遍历当前数字对应的字母（letter）。
    
    return combinations
}