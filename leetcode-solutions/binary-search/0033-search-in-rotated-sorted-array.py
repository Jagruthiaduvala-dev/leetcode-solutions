"""
Problem : 33. Search in Rotated Sorted Array
Link    : https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium
Topic   : Binary Search

Key idea:
    Modified binary search. At every step, at least one half of [left, right]
    is sorted.
      - If nums[left] <= nums[mid], the LEFT half is sorted. If the target lies
        in that sorted range (nums[left] <= target < nums[mid]), search left;
        otherwise search right.
      - Else the RIGHT half is sorted. If the target lies in it
        (nums[mid] < target <= nums[right]), search right; otherwise search left.

Time  : O(log n)
Space : O(1)

Mistakes / Learnings:
    - Decide which half is sorted first, then check whether the target falls inside that sorted half.
    - Use <= in nums[left] <= nums[mid] so a one-element left half is treated as sorted.
    - Range checks must be inclusive on the side of the pointer (nums[left] <= target, target <= nums[right]).
    - mid = left + (right - left) // 2 avoids overflow in other languages.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1