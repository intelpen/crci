
class LLNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

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



class NodeSinglyLinkedList(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def append_to_tail(self, data):
        current_node = self
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = NodeSinglyLinkedList(data)

def delete_node(self, head, node):
    if head == node:
        return head.next
    current = head
    while current.next is not None :
        if current.next == node:
            current.next = current.next.next
            break
        current = current.next
    return head

class SinglyLinkedList(object):
    def __init__(self, data):
        self.head_node = NodeSinglyLinkedList(data)
    def append_to_tail(self, data):
        self.head_node.append_to_tail(data)

if __name__ == "__main__" :
    # define a simple example
    head = NodeSinglyLinkedList(1)
    head.append_to_tail(3)
    head.append_to_tail(3)

    ssl = SinglyLinkedList(4)
    ssl.append_to_tail(3)


