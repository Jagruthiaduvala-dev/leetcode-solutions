"""
Problem : 543. Diameter of Binary Tree
Link    : https://leetcode.com/problems/diameter-of-binary-tree/
Difficulty: Easy
Topic   : Trees (DFS)

Key idea:
    The longest path through any node = height(left) + height(right). Compute
    node heights with DFS, and at every node update a running maximum
    (diameter) with left_h + right_h. The answer is that maximum, since the
    longest path may or may not pass through the root.

Time  : O(n), every node is visited once
Space : O(h) recursion stack, where h = tree height (O(n) worst case, O(log n) balanced)

Mistakes / Learnings:
    - The diameter is measured in EDGES, so left_h + right_h is correct (no +1 or +2).
    - Use nonlocal so the inner function can update the outer diameter variable.
    - The function returns the height (1 + max of children) but records the diameter as a side effect.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            diameter = max(diameter, left_h + right_h)
            return 1 + max(left_h, right_h)

        height(root)
        return diameter