"""
Problem : 45. Jump Game II
Link    : https://leetcode.com/problems/jump-game-ii/
Difficulty: Medium
Topic   : Greedy

Key idea:
    Think of it as BFS over "levels". current_end is the farthest index reachable
    with the jumps taken so far, and farthest is the farthest index reachable with
    one more jump from anything inside the current range. Scan left to right,
    updating farthest. When i reaches current_end, we must take another jump:
    increment jumps and extend current_end to farthest. Stop once current_end
    reaches the last index.

Time  : O(n), single pass
Space : O(1)

Mistakes / Learnings:
    - Loop only to n - 2 (range(n - 1)); no jump is needed once you stand on the last index.
    - Return 0 immediately for a single-element array.
    - A jump is counted only when we reach the end of the current range (i == current_end), not at every step.
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        return jumps