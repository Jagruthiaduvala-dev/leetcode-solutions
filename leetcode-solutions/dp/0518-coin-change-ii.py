"""
Problem : 518. Coin Change II
Link    : https://leetcode.com/problems/coin-change-ii/
Difficulty: Medium
Topic   : Dynamic Programming (Unbounded Knapsack)

Key idea:
    dp[i] = number of combinations that make amount i. Start with dp[0] = 1
    (one way to make 0: use no coins). Loop over coins in the OUTER loop and
    amounts in the inner loop, adding dp[i - coin] to dp[i]. Because each coin
    is fully processed before the next, every combination is counted once
    regardless of order.

Time  : O(n * amount), where n = len(coins)
Space : O(amount)

Mistakes / Learnings:
    - Coins must be the outer loop. Swapping the loops counts permutations
      (1+2 and 2+1 as different), which is the Coin Change / Combination Sum IV pattern.
    - dp[0] = 1 is the base case that everything builds on.
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]