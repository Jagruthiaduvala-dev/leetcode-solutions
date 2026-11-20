"""
Problem : 25. Reverse Nodes in k-Group
Link    : https://leetcode.com/problems/reverse-nodes-in-k-group/
Difficulty: Hard
Topic   : Linked List

Key idea:
    Process the list in groups of k using a dummy head and a group_prev pointer
    (the node just before each group).
      1. Walk k steps from group_prev to find the k-th node. If it doesn't
         exist, fewer than k nodes remain, so stop and return.
      2. Reverse the k nodes in place. prev starts at group_next (the node after
         the group) so the reversed tail connects to the rest of the list.
      3. Reconnect: group_prev.next = kth (the new group head), and move
         group_prev to the old first node of the group (now its tail).

Time  : O(n), each node is visited a constant number of times
Space : O(1), pointers only, no recursion or extra structures

Mistakes / Learnings:
    - Check that k nodes exist BEFORE reversing, so a short last group is left as it is.
    - Set prev = group_next (not None) so the reversed group links to what follows.
    - Save new_group_tail = group_prev.next before relinking; it is the old first node.
    - A dummy node removes the special case for the first group.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            new_group_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_group_tail