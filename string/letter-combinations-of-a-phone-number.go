func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    
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
    
    combinations := []string{""}
    
    for i := 0; i < len(digits); i++ {
        d := digits[i]
        letters, exists := digitMap[d]
        if !exists {
            continue
        }
        
        newCombinations := []string{}
        for _, prefix := range combinations {
            for _, letter := range letters {
                newCombinations = append(newCombinations, prefix+letter)
            }
        }
        combinations = newCombinations
    }
    
    return combinations
}