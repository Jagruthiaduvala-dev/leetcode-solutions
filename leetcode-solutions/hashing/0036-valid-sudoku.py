"""
Problem : 36. Valid Sudoku
Link    : https://leetcode.com/problems/valid-sudoku/
Difficulty: Medium
Topic   : Hashing

Key idea:
    Scan the board once. Keep a set of seen digits for every row, every column
    and every 3x3 box. The box for cell (r, c) is identified by (r // 3, c // 3).
    For each filled cell, if its digit is already in that row's, column's or
    box's set, the board is invalid. Otherwise add it to all three sets.
    Skip empty cells (".").

Time  : O(1), the board is a fixed 9 x 9 (O(n^2) for an n x n board)
Space : O(1), at most 81 digits stored across the sets (O(n^2) in general)

Mistakes / Learnings:
    - Only filled cells are validated; the board does not need to be solvable.
    - Box index (r // 3, c // 3) maps all 9 cells of a 3x3 box to the same key.
    - Use defaultdict(set) so each row/col/box set is created on first use.
"""
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_key = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True