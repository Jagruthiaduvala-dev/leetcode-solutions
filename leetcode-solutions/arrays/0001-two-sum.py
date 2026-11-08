"""
Problem : 1. Two Sum
Link    : https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic   : Hash Map

Key idea:
    Store each number's index in a dict; for each x, check if (target - x) was seen.

Time  : O(n)
Space : O(n)

Mistakes / Learnings:
    - Check the dict BEFORE inserting the current number so an element isn't paired with itself.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
        return []
