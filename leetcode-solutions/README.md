# LeetCode Solutions

My daily LeetCode practice, organized by topic. Each solution file has the problem link, complexity, and the key idea.

## Progress

| Easy | Medium | Hard | Total |
|------|--------|------|-------|
| 5    | 6      | 2    | 13     |

## Solved Problems

| # | Problem | Difficulty | Topic | Time | Space | Date |
|---|---------|-----------|-------|------|-------|------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Hash Map | O(n) | O(n) | 2026-11-08 |
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | Stack / Queue | push O(n), others O(1) | O(n) | 2026-11-08 |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | Stack / Queue | push O(1), pop/peek amortized O(1), empty O(1) | O(n) | 2026-11-09 |
| 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Easy | Strings | O(n·m) | O(m) | 2026-11-14 |
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | DP | O(n·amount) | O(amount) | 2026-11-16 |
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | Trees (DFS) | O(n) | O(h) | 2026-11-17 |
| 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Graphs (BFS) | O(m·n) | O(m·n) | 2026-11-17 |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Backtracking | O(4^n · n) | O(n) | 2026-11-17 |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Backtracking | O(4^n / √n) | O(n) | 2026-11-18 |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Heap / Linked List | O(N log k) | O(k) | 2026-11-18 |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Linked List | O(n) | O(1) | 2026-11-19 |
| 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Trees (DFS) | O(n) | O(h) | 2026-11-19 |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Binary Search | O(log n) | O(1) | 2026-11-19 |
## Structure

```
arrays/        hashing/       two-pointers/   sliding-window/
stack/         binary-search/ linked-list/    trees/
graphs/        heap/          backtracking/   dp/
greedy/        math/          strings/        misc/
```

File naming: `0001-two-sum.py` (4-digit problem number, then slug).

## Notes

- Add a row to the table after every solved problem.
- Keep the "Mistakes / Learnings" comment in each file for revision.
