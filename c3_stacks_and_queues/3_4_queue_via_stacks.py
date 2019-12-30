# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

# Solution we use 2 stack - one input and onw output - the moment when the output stack is empty and a pop is required
# we move the entire input stack in the output one

from c3_stacks_and_queues.stack import Stack

class QueueViaStacks(object):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, data):
        self.in_stack.push(data)

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def peek(self):
        if self.is_empty():
            raise("EmptyQueue")
        if self.out_stack.is_empty():
            return self.in_stack.peek()
        else:
            return  self.out_stack.peek()

    def pop(self):
        if self.is_empty():
            raise("EmptyQueue")
        if self.out_stack.is_empty():
            #if out_stack empty refill from in_stack
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

queue_via_stacks = QueueViaStacks()
queue_via_stacks.push(1)
queue_via_stacks.push(2)
queue_via_stacks.push(3)
print(queue_via_stacks.pop())
print(queue_via_stacks.pop())
queue_via_stacks.push(4)
queue_via_stacks.push(5)
queue_via_stacks.push(6)
print(queue_via_stacks.pop())
print(queue_via_stacks.pop())
print(queue_via_stacks.pop())
print(queue_via_stacks.pop())
