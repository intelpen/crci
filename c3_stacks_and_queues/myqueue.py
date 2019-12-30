from c2_linked_lists.single_linked_list import LLNode
class MyQueue(object):
    def __init__(self):
        self.first = None
        self.last = self.first

    def add(self, data):
        new_first = LLNode(data)
        if self.first is None:
            self.first = self.last = new_first
        else:
            self.first.next = new_first
            self.first = new_first

    def remove(self):
        #remove last
        if self.is_empty():
            raise Exception("EmptyQueue")
        data = self.last.data
        if self.last.next is None:
            self.first = None
        self.last = self.last.next
        return data
    def peek(self):
        # show last element
        if self.is_empty():
            raise Exception("EmptyQueue")
        return self.last.data

    def is_empty(self):
        return self.first == None


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.add(4)
    my_queue.add(6)
    while not my_queue.is_empty():
        print(my_queue.remove())
