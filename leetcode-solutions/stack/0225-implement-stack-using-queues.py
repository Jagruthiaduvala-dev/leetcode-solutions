"""
Problem : 225. Implement Stack using Queues
Link    : https://leetcode.com/problems/implement-stack-using-queues/
Difficulty: Easy
Topic   : Stack / Queue

Key idea:
    Use a single queue. On push, append the new element, then rotate the
    queue (pop from front, append to back) len-1 times so the newest
    element ends up at the front. Then pop/top are just queue operations.

Time  : push O(n), pop O(1), top O(1), empty O(1)
Space : O(n)

"""

from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque() 

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if self.empty():
            raise IndexError("cannot pop from empty stack")
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError("Cannot view top of empty Stack")
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        