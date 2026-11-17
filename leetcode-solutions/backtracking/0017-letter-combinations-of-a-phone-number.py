"""
Problem : 17. Letter Combinations of a Phone Number
Link    : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: Medium
Topic   : Backtracking

Key idea:
    Map each digit to its letters. Backtrack over the digit positions: at
    index i, try every letter for digits[i], append it to the current path,
    recurse to i + 1, then pop it (undo the choice). When index == len(digits)
    the path is a full combination, so join it and add it to the result.

Time  : O(4^n * n), up to 4 letters per digit (7 and 9), and each combination is joined in O(n)
Space : O(n) recursion depth and path, excluding the output list

Mistakes / Learnings:
    - Handle the empty input first: return [] (not [""]).
    - Always pop after the recursive call, that is the "backtrack" step.
    - The path is a list of characters; join it only when it is complete.
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(index: int, current_path: List[str]):
            if index == len(digits):
                result.append("".join(current_path))
                return

            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                current_path.append(letter)
                backtrack(index + 1, current_path)
                current_path.pop()

        backtrack(0, [])
        return result