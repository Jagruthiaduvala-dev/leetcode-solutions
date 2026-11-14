"""
Problem : 28. Find the Index of the First Occurrence in a String
Link    : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy
Topic   : Strings

Key idea:
    Slide a window of length m (len(needle)) across haystack. At each start
    index i, compare haystack[i:i+m] with needle. Return the first i that
    matches, or -1 if none does. Only n - m + 1 start positions are possible.

Time  : O((n - m + 1) * m), roughly O(n * m) in the worst case
Space : O(m) for the temporary slice

Mistakes / Learnings:
    - The loop must run to n - m + 1 (inclusive of the last valid start), or you miss a match at the end.
    - KMP gets this down to O(n + m). Worth learning later for interviews.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1