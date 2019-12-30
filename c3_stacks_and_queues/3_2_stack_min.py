# 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element?
# Push, pop and min should all operate in 0(1) time.

# Solution: The min in o(1) is interesting
# we can have each stack element keep the element and the min
# Other solution would be to keep the minimum for all stack (about 1/n of the  time ... so eventually we would get O(1)
# amortised time even for min

from c2_linked_lists.single_linked_list import LLNode

class StackWithMin(object):

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def min(self):
        if self.is_empty():
            raise Exception("StackEmpty")
        return self.top.data[1]

    def peek(self):
        if self.is_empty():
            raise Exception("StackEmpty")
        return self.top.data[0]

    def push(self, data):
        if self.is_empty():
            self.top = LLNode((data, data)) #min is same as data
        else:
            new_min  = min (data, self.min())
            self.top = LLNode((data, new_min,), self.top)

    def pop(self):
        if self.is_empty():
            raise Exception("StackEmpty")
        else:
            data = self.peek()
            self.top = self.top.next
            return data

stack_with_min = StackWithMin()
stack_with_min.push(4)
stack_with_min.push(1)
stack_with_min.push(3)
stack_with_min.push(0)
while not stack_with_min.is_empty():
    print(f"min:{stack_with_min.min()}")
    print(f"val:{stack_with_min.pop()}")




