"""
Problem : 232. Implement Queue using Stacks
Link    : https://leetcode.com/problems/implement-queue-using-stacks/
Difficulty: Easy
Topic   : Stack / Queue

Key idea:
    Use two stacks (input_stack and output_stack). 
    - Push: Always append to input_stack.
    - Pop/Peek: If output_stack is empty, move all elements from input_stack 
      to output_stack (which reverses their order, giving FIFO behavior).

Time  : push O(1), pop O(1) amortized, peek O(1) amortized, empty O(1)
Space : O(n)

"""

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._move_elements()
        if not self.output_stack:
            raise IndexError("cannot pop from empty queue")
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_elements()
        if not self.output_stack:
            raise IndexError("Cannot view front of empty queue")
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def _move_elements(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())