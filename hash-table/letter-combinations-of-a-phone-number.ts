function letterCombinations(digits: string): string[] {
    if (digits.length === 0) {
        return [];
    }
    
    const digitMap: { [key: string]: string[] } = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    };
    
    let combinations: string[] = [''];
    
    for (const d of digits) {
        const letters = digitMap[d];
        const newCombinations: string[] = [];
        
        for (const prefix of combinations) {
            for (const letter of letters) {
                newCombinations.push(prefix + letter);
            }
        }
        
        combinations = newCombinations;
    }
    
    return combinations;
}