"""
Problem : 1448. Count Good Nodes in Binary Tree
Link    : https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Difficulty: Medium
Topic   : Trees (DFS)

Key idea:
    DFS from the root while carrying the maximum value seen on the path so far.
    A node is "good" if its value >= that path maximum. Count it, update the
    maximum with the node's value, and recurse into both children.

Time  : O(n), every node is visited once
Space : O(h) recursion stack, where h = tree height (O(n) worst case, O(log n) balanced)

Mistakes / Learnings:
    - Pass the max down as a parameter instead of using a global, so each path keeps its own max.
    - Use >= (not >), because a node equal to the path max still counts as good.
    - The root is always good, so start DFS with max_val = root.val.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            count = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        return dfs(root, root.val)