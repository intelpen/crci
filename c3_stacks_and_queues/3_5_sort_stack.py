# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
# Hints:# 15, #32, #43

#Solution - use a second stack

from c3_stacks_and_queues.stack import Stack
def sort(first_stack):
    second_stack = Stack()
    while not first_stack.is_empty():
        tmp = first_stack.pop()
        while  not second_stack.is_empty() and tmp < second_stack.peek() :
            first_stack.push(second_stack.pop())
        second_stack.push(tmp)
    return second_stack

first_stack = Stack()
first_stack.push(1)
first_stack.push(3)
first_stack.push(2)
first_stack.push(4)

second_stack = sort(first_stack)
while not second_stack.is_empty():
    print(second_stack.pop())