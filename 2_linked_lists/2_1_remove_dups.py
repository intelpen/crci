# 2.1 Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# Solution 1. use a hash .... somewhat missing the point
# Solution 2. keep 2 pointers

class LLNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

    def add(self, node):
        current = self
        while current.next is not None:
            current = current.next
        current.next = node

    def add_data(self, data):
        current = self
        while current.next is not None:
            current = current.next
        current.next = LLNode(data, None)

    def delete_node(self, node):
        if self.next == node:
            return self.next
        current = self
        while current.next is not None:
            if current.next == node:
                current.next.next = current.next
                break
            current = current.next
        return current

    def list(self):
        return  [self.data] + (self.next.list() if self.next is not None else [])

def remove_dups(head):
    distinct_values = set()
    distinct_values.add(head.data)
    current = head
    while current.next is not None:
        if current.next.data in distinct_values:
            current.next = current.next.next
        else:
            distinct_values.add(current.data)
            current = current.next
    return head

def remove_dups_no_buffer(head):
    current = head
    runner = head
    while current.next is not None:
        runner = current
        while  runner.next.next is not None:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

    return head



head = LLNode(3)
head.add_data(4)
head.add_data(6)
head.add_data(4)
head.add_data(4)
head.add_data(8)

print(head.list())

print(remove_dups_no_buffer(head).list())