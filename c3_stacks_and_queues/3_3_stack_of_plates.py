# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
# Hints:#64, #87

from c3_stacks_and_queues.stack import Stack
class SetOfStacks():
    def __init__(self, stack_capacity = 3):
        first_stack =Stack()
        self.stack_capacity = stack_capacity
        self.stacks_list = [first_stack]

    def no_stacks(self):
        return len(self.stacks_list)

    def top_stack(self):
        return self.stacks_list[self.no_stacks()-1]

    def is_empty(self):
        return self.no_stacks() ==1 and self.top_stack().is_empty()

    def push(self, data):
        curr_stack = self.top_stack()
        if curr_stack.size() >= self.stack_capacity:
            last_stack = Stack()
            last_stack.push(data)
            self.stacks_list.append(last_stack)
        else:
            curr_stack.push(data)

    def pop(self):
        if self.is_empty():
            raise("EmptySetOFStacks")
        else:
            curr_stack = self.top_stack()
            if curr_stack.is_empty():
                self.stacks_list.remove(curr_stack)
                curr_stack = self.top_stack()
            data = curr_stack.pop()
            return data

    def peek(self):
        if self.is_empty():
            raise ("EmptySetOFStacks")
        else:
            curr_stack = self.top_stack()
            return curr_stack.peek()

    def pop_at(self, stack_index):
        # normally we can just pop from that  stack .. no need to  fil it afterwards
        if self.no_stacks() < stack_index:
            raise Exception("StackNotExisting")
        else:
            curr_stack = self.stacks_list[stack_index]
            while curr_stack.is_empty():
                self.stacks_list.remove(curr_stack)
                stack_index -= 1
                if stack_index <0:
                    raise Exception("No elements before that stack which is empty")
                curr_stack = self.stacks_list[stack_index]
            return curr_stack.pop()


set_of_stacks = SetOfStacks(2)
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)
set_of_stacks.push(6)
set_of_stacks.push(7)
print(len(set_of_stacks.stacks_list))
print(set_of_stacks.pop_at(1))
while not set_of_stacks.is_empty():
    print(set_of_stacks.pop())
    #print(set_of_stacks)






