"""
Problem : 23. Merge k Sorted Lists
Link    : https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard
Topic   : Heap / Linked List

Key idea:
    Keep a min-heap holding the current head of each list. Repeatedly pop the
    smallest node, attach it to the result, and push that node's next node
    (if any) onto the heap. The heap never holds more than k nodes, so each
    step costs O(log k).

Time  : O(N log k), where N = total number of nodes and k = number of lists
Space : O(k) for the heap (the result reuses the existing nodes)

Mistakes / Learnings:
    - Heap entries are (val, i, node). The list index i is a tie-breaker: if two
      values are equal, Python would otherwise try to compare ListNode objects and crash.
    - Use a dummy head node so you don't need a special case for the first node.
    - Skip empty lists (None) when building the initial heap.
"""
import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next