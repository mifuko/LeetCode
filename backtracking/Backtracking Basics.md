Here's a comprehensive overview of **Backtracking Algorithms** in English, formatted with Markdown for easy reference:


# **Backtracking Basics**
Backtracking is a general algorithmic technique for **incrementally building candidates to solutions**, and **abandoning a candidate ("backtracking")** as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## **Core Concepts**
1. **Recursive Exploration**: Use recursion to explore all possible paths.
2. **State Management**: Track the current path/state during recursion.
3. **Pruning**: Terminate invalid paths early to avoid unnecessary computation.
4. **Backtracking Step**: Undo the most recent choice if it leads to a dead end.


# **Typical Problem Types**
1. **Combinatorial Search Problems**
   - Find all valid combinations/permutations that meet constraints.
   - Examples:
     - [Combination Sum](https://leetcode.com/problems/combination-sum/)
     - [Subsets](https://leetcode.com/problems/subsets/)
     - [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

2. **Constraint Satisfaction Problems (CSP)**
   - Find solutions that satisfy a set of constraints.
   - Examples:
     - [N-Queens](https://leetcode.com/problems/n-queens/)
     - [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
     - [Word Search](https://leetcode.com/problems/word-search/)

3. **Pathfinding Problems**
   - Find paths in grids/graphs with specific conditions.
   - Examples:
     - [Maze Pathfinding](https://leetcode.com/problems/unique-paths/)
     - [Hamiltonian Path](https://en.wikipedia.org/wiki/Hamiltonian_path_problem)


# **Backtracking Template**
A typical backtracking algorithm follows this structure:

```python
def backtrack(path, choices):
     Base case: if path is valid, add to results
    if is_valid(path):
        results.append(path.copy())
        return
    
     Explore all possible choices
    for choice in choices:
         Prune invalid choices early
        if not is_valid_choice(path, choice):
            continue
        
         Make the choice
        path.append(choice)
        
         Recurse with updated path
        backtrack(path, remaining_choices)
        
         Undo the choice (backtrack)
        path.pop()
```


# **Key Components**
1. **Termination Condition**: When to stop and collect results.
2. **Choice List**: All possible options at each step.
3. **State Transition**: Update the current state (path) after each choice.
4. **Backtracking**: Restore the previous state to explore alternative paths.


# **Optimization Techniques**
1. **Sorting**: Sort candidates to facilitate pruning (e.g., avoid duplicates).
2. **Early Termination**: Stop recursion when further paths are guaranteed invalid.
3. **Use of Hash Tables/Sets**: Track visited states to avoid redundant computations.
4. **Bitmasking**: Efficiently represent states using bits (e.g., N-Queens).


# **Comparison with Other Algorithms**
| **Algorithm**   | **Use Case**                              | **Core Idea**                                |
|-----------------|-------------------------------------------|---------------------------------------------|
| **Backtracking**| Enumerate all valid solutions             | Recursively explore all paths, prune early  |
| **Dynamic Programming**| Optimize overlapping subproblems       | Cache results to avoid重复计算               |
| **Greedy**      | Find locally optimal solutions           | Choose the best immediate option, no backtracking |
| **BFS/DFS**     | Traverse graphs/grids                    | Systematically explore nodes                |


# **Example Problems & Solutions**

## **1. Combination Sum (LeetCode 39)**
**Problem**: Find all unique combinations that sum to `target` (elements can be reused).

**Solution Code**:
```python
def combinationSum(candidates, target):
    results = []
    def backtrack(remain, path, start):
        if remain == 0:
            results.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                continue   Prune: skip if current candidate exceeds remaining
            path.append(candidates[i])
            backtrack(remain - candidates[i], path, i)   Allow reuse of same element
            path.pop()   Backtrack
    backtrack(target, [], 0)
    return results
```

## **2. N-Queens (LeetCode 51)**
**Problem**: Place `n` queens on an `n×n` board such that no two attack each other.

**Solution Code**:
```python
def solveNQueens(n):
    results = []
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            results.append(generate_board(cols, n))
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue   Prune: invalid placement
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            backtrack(row + 1, cols, diag1, diag2)
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)
    backtrack(0, set(), set(), set())
    return results
```


# **Key Takeaways**
1. **When to Use Backtracking**:
   - Problems requiring **all possible solutions** (not just optimal).
   - Solutions can be built incrementally with clear constraints.

2. **Efficiency**:
   - Time complexity is often exponential (e.g., O(2ⁿ) or O(n!)) due to exhaustive search.
   - Optimize via pruning and state tracking.

3. **Practice Problems**:
   - [Subsets](https://leetcode.com/problems/subsets/)
   - [Permutations](https://leetcode.com/problems/permutations/)
   - [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
   - [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)


# **Resources for Further Learning**
- LeetCode's [Backtracking Problems](https://leetcode.com/tag/backtracking/)
- Stanford's [Recursion & Backtracking Notes](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/handouts/18-recursion-backtracking.pdf)
- Introduction to Algorithms (CLRS) - Chapter 15 (Dynamic Programming) and Chapter 34 (NP-Completeness)
