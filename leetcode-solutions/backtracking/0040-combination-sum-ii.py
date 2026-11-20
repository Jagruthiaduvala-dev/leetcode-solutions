"""
Problem : 40. Combination Sum II
Link    : https://leetcode.com/problems/combination-sum-ii/
Difficulty: Medium
Topic   : Backtracking

Key idea:
    Same backtracking as Combination Sum, with two changes because each number
    can be used only ONCE and the input may contain duplicates:
      - recurse with i + 1 (move past the number just used)
      - skip duplicates at the same level: if i > start and
        candidates[i] == candidates[i - 1], continue
    Sort first so equal numbers sit next to each other and the early break works.

Time  : O(2^n) in the worst case (each number is either taken or skipped), times O(n) to copy a result
Space : O(n) recursion depth and current path, excluding the output

Mistakes / Learnings:
    - The duplicate check must be i > start (same loop level), not i > 0, or valid combos like [1, 1, 6] get dropped.
    - Use i + 1 in the recursive call because each element is used at most once.
    - Sorting is what makes the "skip equal neighbour" trick work.
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []
        current: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                if num > remaining:
                    break
                current.append(num)
                backtrack(i + 1, remaining - num)
                current.pop()

        backtrack(0, target)
        return result