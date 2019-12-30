# Three in One: Describe how you could use a single array to implement three stacks.

# Solutions options:
# For a stack I would keep at a[0] the height of the stack and at then the stack
# For 3 stacks , we asign n/3 as the start of each stack

class ThreeStacks(object):
    def __init__(self, capacity_per_stack = 10):
        self.storage = [None]*capacity_per_stack*3
        self.capacity_per_stack = capacity_per_stack
        self.sizes= [0,0,0]

    def push(self,stack_no,data):
        start_stack = self.capacity_per_stack * stack_no
        self.storage[start_stack+self.sizes[stack_no]] = data
        self.sizes[stack_no] +=1

    def pop(self, stack_no):
        if self.is_empty(stack_no):
            raise Exception(f"Stack {stack_no}")
        data = self.storage[self.capacity_per_stack * stack_no + self.sizes[stack_no]-1]
        self.storage[self.capacity_per_stack * stack_no + self.sizes[stack_no] - 1] = None
        self.sizes[stack_no] -=1
        return data

    def is_empty(self, stack_no):
        return self.sizes[stack_no] == 0

    def peek(self, stack_no):
        if self.is_empty(stack_no):
            raise Exception(f"Stack {stack_no}")
        data = self.storage[self.capacity_per_stack * stack_no + self.sizes[stack_no]-1]
        return data


my_stack = ThreeStacks(capacity_per_stack=3)
my_stack.push(0,1)
my_stack.push(1,1)
my_stack.push(2,1)
my_stack.push(0,2)
my_stack.push(1,2)
my_stack.push(2,2)
print(my_stack.storage)
print(my_stack.pop(1))
print(my_stack.pop(2))
print(my_stack.pop(2))
my_stack.push(2,6)
print(my_stack.storage)