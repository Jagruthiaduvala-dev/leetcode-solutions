"""
Problem : 43. Multiply Strings
Link    : https://leetcode.com/problems/multiply-strings/
Difficulty: Medium
Topic   : Math / Strings

Key idea:
    Grade-school multiplication. The product of an m-digit and an n-digit number
    has at most m + n digits, so use a result array of that size. Multiply every
    digit pair (i, j); the product lands at positions i + j (carry) and i + j + 1
    (digit). Add the existing value at i + j + 1, store total % 10 there, and add
    the carry (total // 10) into i + j. Finally skip leading zeros and join.

Time  : O(m * n)
Space : O(m + n) for the result array

Mistakes / Learnings:
    - Handle "0" up front, otherwise the result would be a string of zeros.
    - Iterate from the right (last digit first), like multiplying by hand.
    - Strip leading zeros before joining the digits.
    - Position i + j + 1 holds the digit and i + j receives the carry.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord("0")
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord("0")

                total = d1 * d2 + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return "".join(str(x) for x in res[start:])