"""
Problem : 994. Rotting Oranges
Link    : https://leetcode.com/problems/rotting-oranges/
Difficulty: Medium
Topic   : Graphs (Multi-source BFS)

Key idea:
    Put ALL rotten oranges in the queue at once (multi-source BFS), each with
    time 0, and count the fresh ones. Each BFS step rots the 4-directional fresh
    neighbours, marks them rotten, reduces the fresh count and enqueues them
    with time + 1. The time of the last orange to rot is the answer. If fresh
    oranges are left at the end, some were unreachable, so return -1.

Time  : O(m * n), each cell is enqueued at most once
Space : O(m * n) for the queue in the worst case

Mistakes / Learnings:
    - Start from every rotten orange together, not one at a time, so the minutes are counted in parallel.
    - Check fresh_count == 0 up front and return 0 (no fresh oranges means no time needed).
    - Mark a cell as rotten when it is ENQUEUED, not when popped, to avoid adding it twice.
    - Final check is fresh_count == 0, otherwise -1.
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, minutes + 1))

        return minutes if fresh_count == 0 else -1