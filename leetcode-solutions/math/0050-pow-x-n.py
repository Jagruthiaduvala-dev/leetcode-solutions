"""
Problem : 50. Pow(x, n)
Link    : https://leetcode.com/problems/powx-n/
Difficulty: Medium
Topic   : Math (Binary Exponentiation)

Key idea:
    Fast exponentiation (exponentiation by squaring). Write |n| in binary: for
    each bit, if it is 1 multiply the result by the current base; then square the
    base and shift the exponent right by one. This needs only O(log n)
    multiplications. For negative n, invert the base first (x^-n = (1/x)^n).
    Decimal with 50 digits of precision is used to avoid floating point error
    building up across the repeated squaring.

Time  : O(log |n|)
Space : O(1)

Mistakes / Learnings:
    - Handle negative exponents by inverting the base and using abs(n).
    - exp & 1 checks the lowest bit; exp >>= 1 moves to the next bit.
    - n == 0 returns 1.0 immediately.
    - Plain floats also work for most inputs; Decimal is just extra precision.
"""
from decimal import Decimal, localcontext


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        with localcontext() as ctx:
            ctx.prec = 50
            base = Decimal(str(x))
            exp = abs(n)

            if n < 0:
                base = Decimal(1) / base

            result = Decimal(1)
            while exp > 0:
                if exp & 1:
                    result *= base
                base *= base
                exp >>= 1

            return float(result)