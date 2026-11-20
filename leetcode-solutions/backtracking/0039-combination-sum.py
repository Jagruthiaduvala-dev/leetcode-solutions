"""
Problem : 39. Combination Sum
Link    : https://leetcode.com/problems/combination-sum/
Difficulty: Medium
Topic   : Backtracking

Key idea:
    Sort the candidates, then backtrack with a start index and the remaining
    sum. At each step try every candidate from index `start` onward. Recursing
    with the SAME index i (not i + 1) lets a number be reused unlimited times,
    while never going back to smaller indices avoids duplicate combinations in
    a different order. If remaining == 0, save a copy of the current path.
    Because the list is sorted, break as soon as a number exceeds remaining.

Time  : O(N^(T/M)), N = number of candidates, T = target, M = smallest candidate
Space : O(T/M) recursion depth (the maximum number of numbers in one combination)

Mistakes / Learnings:
    - Recurse with i (not i + 1) because the same number can be reused.
    - Save current.copy(), not current, since the list keeps changing.
    - Sorting lets you break early instead of continuing through larger numbers.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []
        current: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remaining:
                    break
                current.append(num)
                backtrack(i, remaining - num)
                current.pop()

        backtrack(0, target)
        return result