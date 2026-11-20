"""
Problem : 22. Generate Parentheses
Link    : https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium
Topic   : Backtracking

Key idea:
    Build the string one character at a time, tracking how many "(" and ")"
    have been used. Two rules keep every string valid:
      - add "(" only if open_count < n
      - add ")" only if close_count < open_count
    When the length reaches 2 * n, the string is a complete valid combination.

Time  : O(4^n / sqrt(n)) combinations (Catalan number), times O(n) to build each string
Space : O(n) recursion depth and path, excluding the output list

Mistakes / Learnings:
    - Never add ")" unless there is an unmatched "(" (close_count < open_count), or the string becomes invalid.
    - Always pop after the recursive call to undo the choice.
    - Pruning invalid choices early is better than generating everything and filtering.
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current: List[str]):
            if len(current) == 2 * n:
                res.append("".join(current))
                return

            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count, current)
                current.pop()

            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1, current)
                current.pop()

        backtrack(0, 0, [])
        return res