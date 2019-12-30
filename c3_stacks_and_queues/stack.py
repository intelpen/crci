from c2_linked_lists.single_linked_list import LLNode
class Stack(object):

    def __init__(self):
        self.top = None
        self._size = 0

    def size(self):
        return self._size

    def pop(self):
        if self.top is None:
            raise Exception("EmptyStackException")
        data = self.top.data
        self._size -=1
        self.top = self.top.next
        return data

    def push(self, data):
        self._size +=1
        self.top = LLNode(data, self.top)

    def peek(self):
        if self.top is None:
            raise Exception("EmptyStackException")
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(3)
    while not stack.is_empty():
        print(stack.pop())
